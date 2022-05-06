# Carta Maior | IA - Facthus 2022/01
### Implemente um jogo de cartas “Carta Maior” com as seguintes regras:

1. O jogo é composto por 2 jogadores que recebem, cada um, 5 cartas de um
baralho comum (52 cartas, 13 cartas de cada naipe).

2. O jogador 1 inicia o jogo, selecionando uma de suas cartas para jogar.

3. O jogador 2 seleciona, então, uma de suas cartas para jogar, de acordo com
o seguinte critério: deve jogar uma carta do mesmo naipe, caso possua ou
jogar uma carta de outro naipe somente quando não possuir cartas com o
naipe da carta escolhida pelo adversário.

4. Vence a rodada o jogador que jogou a maior carta (caso ambas sejam do
mesmo naipe) ou o jogador que jogou o “naipe da vez” (naipe da primeira
carta jogada na rodada).

5. As cartas devem ser comparadas na seguinte ordem (da menor para a
maior): 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.

6. O jogador que venceu a rodada escolhe uma carta para iniciar a próxima
rodada, seguindo as mesmas regras. Vence a partida o jogador que venceu o
maior número de rodadas.

## Requisitos

```bash
1. pip install numpy

```