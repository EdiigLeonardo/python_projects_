# importar tudo
import projeto_2048

# definir novas funções:
from projeto_2048.logic import *


def pede_jogada():
    jogada = str(input('Introduza uma jogada (N,S,W,E): '))
    print()
    return jogada


def cria_tabuleiro(tamanho_grelha=4):
    tab = tabuleiro(tamanho_grelha)
    return tab


def jogo_2048():
    print('#'*100)
    print('2048!! seja bem vindo:'.center(50))
    jogadas_possiveis = ['N','S','E','W','n','s','w','e']
    """pede_tamanho = int(input(' Indique o tamanho da grelha (4,5,6,7,8): '))
    if pede_tamanho <4:
        print('#' * 100)
        print('#' * 50,'Bem Vindo ao modo programador, esse modo é só para teste'.center(50),'#' * 50)"""
    tab_jogo = cria_tabuleiro(10)
    preenche_dois_aleatorio(tab_jogo)
    preenche_dois_aleatorio(tab_jogo)
    while True:
        escreve_tabuleiro(tab_jogo)
        movimento = pede_jogada()
        tab_2 = tabuleiro(tabuleiro=tab_jogo)
        try:
            tabuleiro_reduz(tab_jogo,movimento)
            if not tabuleiros_iguais(tab_jogo,tab_2):
                preenche_posicao_aleatoria(tab_jogo)
            if tabuleiro_terminado(tab_jogo):
                print('Jogo Terminado'.center(10))
            print('#' * 100)
            print('')
        except ValueError as err:
            print(err)


jogo_2048()

