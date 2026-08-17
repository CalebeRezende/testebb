"""
Autoclicker para dar "amei" na live do TikTok sem precisar ficar
tocando a tela/mouse sem parar.

Como funciona:
  1. Abra a live do seu pai no TikTok (navegador ou app), do jeito
     que voce normalmente assiste.
  2. Rode este script (veja instrucoes no README.md).
  3. Posicione o mouse em cima do coracao/botao "amei" da live e
     aperte F8 para salvar essa posicao.
  4. Aperte F6 para ligar/desligar os cliques automaticos.
  5. Aperte ESC a qualquer momento para encerrar o script.

Uso pessoal, em baixa escala, na sua propria conta. Nao deixe
rodando por horas sem supervisao nem use em varias contas -
isso pode ser tratado pelo TikTok como manipulacao de engajamento
e sua conta pode ser penalizada.
"""

import random
import sys
import threading
import time

import pyautogui
from pynput import keyboard

# Intervalo entre cliques, em segundos. Um pequeno "jitter" aleatorio
# e' somado para nao ficar em um ritmo perfeitamente robotico.
INTERVALO_BASE = 1.2
JITTER = 0.4

pyautogui.FAILSAFE = True  # mover o mouse pro canto superior esquerdo cancela cliques

posicao_alvo = None
clicando = False
rodando = True


def loop_de_cliques():
    while rodando:
        if clicando and posicao_alvo is not None:
            x, y = posicao_alvo
            try:
                pyautogui.click(x=x, y=y)
            except pyautogui.FailSafeException:
                print("\n[!] Failsafe acionado (mouse no canto). Cliques pausados.")
                pausar()
            time.sleep(INTERVALO_BASE + random.uniform(-JITTER, JITTER))
        else:
            time.sleep(0.1)


def pausar():
    global clicando
    clicando = False


def alternar_clicando():
    global clicando
    if posicao_alvo is None:
        print("[!] Nenhuma posicao definida ainda. Aperte F8 em cima do botao 'amei' primeiro.")
        return
    clicando = not clicando
    estado = "LIGADO" if clicando else "PAUSADO"
    print(f"[*] Autoclicker {estado}. Posicao: {posicao_alvo}")


def definir_posicao():
    global posicao_alvo
    posicao_alvo = pyautogui.position()
    print(f"[*] Posicao salva: {posicao_alvo}. Aperte F6 para ligar/desligar os cliques.")


def encerrar():
    global rodando, clicando
    clicando = False
    rodando = False
    print("\n[*] Encerrando. Ate mais!")
    sys.exit(0)


def ao_pressionar(tecla):
    if tecla == keyboard.Key.f8:
        definir_posicao()
    elif tecla == keyboard.Key.f6:
        alternar_clicando()
    elif tecla == keyboard.Key.esc:
        encerrar()


def main():
    print("=== Autoclicker de live do TikTok ===")
    print("F8  -> marcar a posicao do botao 'amei' (posicione o mouse antes)")
    print("F6  -> ligar/desligar os cliques automaticos")
    print("ESC -> encerrar o programa")
    print()

    thread = threading.Thread(target=loop_de_cliques, daemon=True)
    thread.start()

    with keyboard.Listener(on_press=ao_pressionar) as listener:
        listener.join()


if __name__ == "__main__":
    main()
