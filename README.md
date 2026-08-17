# Autoclicker para live do TikTok

Script simples (Windows e Linux) que fica clicando automaticamente em
um ponto fixo da tela (o botao de coracao/"amei" da live), pra voce
nao precisar tocar sem parar e cansar o dedo.

E' o mesmo arquivo `tiktok_live_autoclicker.py` para os dois sistemas
- so muda a forma de instalar as dependencias.

## Instalacao - Windows

1. Instale o Python 3.9+ (https://www.python.org/downloads/) e marque
   a opcao "Add python.exe to PATH" no instalador.
2. Abra o PowerShell ou CMD na pasta do projeto e rode:

```
pip install -r requirements.txt
```

## Instalacao - Linux

1. Instale Python 3 e o pip (normalmente ja vem instalado; se nao):

```
sudo apt install python3 python3-pip python3-venv   # Debian/Ubuntu
sudo dnf install python3 python3-pip                # Fedora
```

2. (Recomendado) crie um ambiente virtual e instale as dependencias:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Importante - X11 vs Wayland:** o script usa `pyautogui`/`pynput`,
   que so funcionam em sessoes **X11**. Se sua distro usa Wayland por
   padrao (Ubuntu, Fedora recentes), verifique/troque para "Ubuntu on
   Xorg" (ou equivalente) na tela de login antes de rodar o script.
   Para checar qual voce esta usando:

```
echo $XDG_SESSION_TYPE
```

   Se aparecer `wayland`, troque a sessao para X11/Xorg no login.

## Como usar

1. Abra a live do seu pai no TikTok (navegador ou app) e deixe a
   janela visivel, sem minimizar.
2. Rode o script:

```
python tiktok_live_autoclicker.py
```

3. Posicione o cursor do mouse exatamente em cima do botao de
   coracao/"amei" da live.
4. Aperte **F8** para salvar essa posicao.
5. Aperte **F6** para ligar os cliques automaticos (aperte de novo
   para pausar).
6. Aperte **ESC** a qualquer momento para fechar o programa.

Se voce mover a janela do TikTok ou mudar de tela, marque a posicao
de novo com F8.

## Observacoes

- O clique e' feito na posicao exata da tela, entao **nao mexa o
  mouse** enquanto o autoclicker estiver ligado, ou ele vai clicar
  no lugar errado.
- Mover o mouse para o canto superior esquerdo da tela pausa os
  cliques automaticamente (failsafe do pyautogui) - util se algo
  sair do controle.
- Use com moderacao: e' uma ferramenta pra facilitar o uso pessoal
  (evitar dor no dedo), nao para deixar rodando 24h por dia. Cliques
  automatizados em excesso podem ser entendidos pela plataforma como
  manipulacao de engajamento e sua conta pode sofrer restricoes.
