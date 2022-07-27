from typing import Dict, List, Tuple, Set

names: list[str] = ['Ewerton', 'lauren']

versoes: tuple[int] = (1, 2, 3)

opcoes: dict[int, str] = {1: 'Bundinha', 2:'Rabicó'}

valores: set[int] = {3, 4, 5, 6}


import random

# https://www.alt-codes.net/suit-cards.php

naipes = '♠ ♥ ♣ ♦ ♤ ♡ ♧ ♢'.split()
cartas = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    # Cria uma baralho com 52 cartas para jogar
    baralho = [(n, c) for c in cartas for n in naipes]
    if  aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    # Gerencia a mão de cartas de acordo com o baralho gerado
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    # Inicia um jogo de cartas para 4 jogadores
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao  in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f'{j}{c}' for(j,c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

