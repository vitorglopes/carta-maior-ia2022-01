from dataclasses import replace
import numpy as np

nomeCarta = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
naipes = ['E', 'P', 'C', 'O']

def exibe(texto):
    print(texto + '\n')

def definirCartas():

    cartas = []

    for n in naipes:
        for c in nomeCarta:
            cartas.append(c + ' ' + n)
    return cartas

def pesoCarta(cartaJogada):
    busca = cartaJogada[0:2]
    buscaNaipe = cartaJogada[2:4]
    print(buscaNaipe)

def main():
    exibe('........................................')

    jogador1 = input('Jogador 1, defina seu nome: ')
    jogador2 = input('Jogador 2, defina seu nome: ')
    cartasj1 = []
    cartasj2 = []
    pontosj1 = 0
    pontosj2 = 0

    exibe('\nBem-vindos ao Carta Maior!')
    exibe(jogador1 + ' X ' + jogador2)

    cartas = definirCartas();

    exibe('Jogador ' + jogador1 + ' recebendo as cartas....')
    cartasj1 = np.random.choice(cartas, size=5, replace=False)
    
    exibe('Jogador ' + jogador2 + ' recebendo as cartas....')
    cartasj2 = np.random.choice(cartas, size=5, replace=False)
    
    print('cartas p2: ', cartasj2)
    

main()



