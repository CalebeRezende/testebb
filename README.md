# Autoclicker para live do TikTok

Script simples para Windows que fica clicando automaticamente em um
ponto fixo da tela (o botao de coracao/"amei" da live), pra voce nao
precisar tocar sem parar e cansar o dedo.

## Instalacao

1. Tenha Python 3.9+ instalado (https://www.python.org/downloads/).
2. Abra o terminal (PowerShell ou CMD) na pasta do projeto e rode:

```
pip install -r requirements.txt
```

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
