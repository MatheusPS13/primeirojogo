# Primeiro jogo

Exercício de projeto de programação.Jogo 2D de cobra que cresce em mundo quadrado e limitado.


## Classes

### Interface

3 classes

- Tela de início 

Objeto de `tkinter` com um menu de opções para novo jogo, salvar, carregar, e configurações.

- Tela de configurações

Objeto de `tkinter` para mudar dificuldade e velocidade do jogo.

- Jogo

Objeto de `pygame` que contém a mecânica do jogo e a sua interface.



### Elementos do jogo

3 classes

- Cobra

Controlado pelo jogador pelo teclado com objetivo de procurar alimento e não colidir.
O tamanho cresce quando encontra alimento.

- Alimento

Objeto visual consumido pela cobra para crescer quando sua cabeça o sobrepõe.

- Estado do jogo

Informações que presentam o jogo para salvar e carregar de volta.