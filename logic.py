# funcoes gerais
import random


def e_coordenada(outro):
    if isinstance(outro, coordenada):
        return True
    return False


def e_tabuleiro(objecto):
    if isinstance(objecto, tabuleiro):
        return True
    else:
        return False


def escreve_tabuleiro(tabuleiro):
    tab = tabuleiro.get_tabuleiro()
    print('Pontuação: ', (tabuleiro.tabuleiro_pontuacao()))
    print()
    for i in tab:
        for j in range(len(tab[0])):
            print('[' + str(i[j]).center(5) + ']', end=' ')
        print('')
    # return (tabuleiro.tabuleiro_pontuacao())


def tabuleiro_preenche_posicao(tabuleiro, cord, v):
    linha = cord.coordenada_linha()
    coluna = cord.coordenada_coluna()
    if e_coordenada(cord) and isinstance(v, int):
        tabuleiro.atualiza_posicao_tabuleiro(linha - 1, coluna - 1, v)
    return tabuleiro


def actualiza_pontuacao(tabuleiro, v):
    if v % 4 == 0 and v > 0:
        tabuleiro.set_potuacao(v)
    return tabuleiro

def tem_jogada(tab_1):
    tab_2 = tabuleiro(tabuleiro=tab_1)
    tabuleiro_reduz(tab_2, 'w')
    tabuleiro_reduz(tab_2, 'e')
    tabuleiro_reduz(tab_2, 'n')
    tabuleiro_reduz(tab_2, 's')
    if tabuleiros_iguais(tab_1,tab_2):
        return False
    return True

def tabuleiro_terminado(tabuleiro):
    tab = tabuleiro.get_tabuleiro()
    medidor = False
    if not tem_jogada(tabuleiro):
        medidor = True
    for linha in range(len(tab)):
        for coluna in range(len(tab[0])):
            if tab[linha][coluna] == 2048:
                print('Parabéns!!!, você venceu!'.center(5))
    return medidor


def tabuleiros_iguais(tabuleiro_1, tabuleiro_2):
    tab_1 = tabuleiro_1.get_tabuleiro()
    tab_2 = tabuleiro_2.get_tabuleiro()
    if tab_1 != tab_2:
        return False
    return True


def preenche_posicao_aleatoria(tabuleiro):
    zeros = tabuleiro.tabuleiro_posicoes_zero()
    numeros = random.choice([2, 4])
    crd = tuple(random.choice(zeros))
    cordenada_aux = coordenada(crd[0], crd[1])
    tabuleiro_preenche_posicao(tabuleiro, cordenada_aux, numeros)
    return tabuleiro

def preenche_dois_aleatorio(tabuleiro):
    zeros = tabuleiro.tabuleiro_posicoes_zero()
    numeros = 2
    crd = tuple(random.choice(zeros))
    cordenada_aux = coordenada(crd[0], crd[1])
    tabuleiro_preenche_posicao(tabuleiro, cordenada_aux, numeros)
    return tabuleiro

def tabuleiro_reduz(tabuleiro, movimento):
    tab = tabuleiro.get_tabuleiro()
    pontuacao = 0
    if movimento == 'N'.lower() or movimento == 'N':
        for ciclo in range(len(tab)):
            for coluna in range(len(tab[0])):
                for linha in range(len(tab) - 1):
                    if tab[linha][coluna] == 0 and tab[linha + 1][coluna] != 0:
                        cord_aux = coordenada(linha + 1, coluna + 1)
                        cord_aux_2 = coordenada(linha + 2, coluna + 1)
                        aux = tab[linha + 1][coluna]
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
        for coluna in range(len(tab[0])):
            for linha in range(len(tab) - 1):
                if tab[linha][coluna] != 0 and tab[linha + 1][coluna] == tab[linha][coluna]:
                    cord_aux = coordenada(linha + 1, coluna + 1)
                    cord_aux_2 = coordenada(linha + 2, coluna + 1)
                    aux = tab[linha + 1][coluna] + tab[linha + 1][coluna]
                    tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                    tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
                    pontuacao += aux
        for ciclo in range(len(tab)):
            for coluna in range(len(tab[0])):
                for linha in range(len(tab) - 1):
                    if tab[linha][coluna] == 0 and tab[linha + 1][coluna] != 0:
                        cord_aux = coordenada(linha + 1, coluna + 1)
                        cord_aux_2 = coordenada(linha + 2, coluna + 1)
                        aux = tab[linha + 1][coluna]
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
        actualiza_pontuacao(tabuleiro, pontuacao)
        return tabuleiro
    elif movimento == 'S'.lower() or movimento == 'S':
        for ciclo in range(len(tab)):
            for coluna in range(len(tab[0])):
                for linha in range(len(tab) - 1):
                    linha = len(tab) - 1 - linha
                    if tab[linha][coluna] == 0 and tab[linha - 1][coluna] != 0:
                        aux = tab[linha - 1][coluna]
                        tab[linha][coluna] = aux
                        tab[linha - 1][coluna] = 0
                        coordenada_aux = coordenada(linha, coluna + 1)
                        coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
        for coluna in range(len(tab[0])):
            for linha in range(len(tab) - 1):
                linha = len(tab) - 1 - linha
                if tab[linha][coluna] == tab[linha - 1][coluna] and tab[linha - 1][coluna] != 0:
                    aux = tab[linha - 1][coluna] + tab[linha][coluna]
                    tab[linha][coluna] = aux
                    tab[linha - 1][coluna] = 0
                    coordenada_aux = coordenada(linha, coluna + 1)
                    # coordenada_aux.mostra_cord()
                    coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                    # coordenada_aux_2.mostra_cord()
                    tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                    tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
                    pontuacao += aux
        for ciclo in range(len(tab)):
            for coluna in range(len(tab[0])):
                for linha in range(len(tab) - 1):
                    linha = len(tab) - 1 - linha
                    if tab[linha][coluna] == 0 and tab[linha - 1][coluna] != 0:
                        aux = tab[linha - 1][coluna]
                        tab[linha][coluna] = aux
                        tab[linha - 1][coluna] = 0
                        coordenada_aux = coordenada(linha, coluna + 1)
                        coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
        actualiza_pontuacao(tabuleiro, pontuacao)
        return tabuleiro
    elif movimento == 'W' or movimento == 'w':
        for ciclo in range(len(tab)):
            for linha in range(len(tab)):
                for coluna in range(len(tab[0]) - 1):
                    if tab[linha][coluna] == 0 and tab[linha][coluna + 1] != 0:
                        cord_aux = coordenada(linha + 1, coluna + 1)
                        cord_aux_2 = coordenada(linha + 1, coluna + 2)
                        aux = tab[linha][coluna + 1]
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
        for linha in range(len(tab)):
            for coluna in range(len(tab[0]) - 1):
                if tab[linha][coluna] != 0 and tab[linha][coluna + 1] == tab[linha][coluna]:
                    cord_aux = coordenada(linha + 1, coluna + 1)
                    cord_aux_2 = coordenada(linha + 1, coluna + 2)
                    aux = tab[linha][coluna + 1] + tab[linha][coluna + 1]
                    tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                    tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
                    pontuacao += aux
        for ciclo in range(len(tab)):
            for linha in range(len(tab)):
                for coluna in range(len(tab[0]) - 1):
                    if tab[linha][coluna] == 0 and tab[linha][coluna + 1] != 0:
                        cord_aux = coordenada(linha + 1, coluna + 1)
                        cord_aux_2 = coordenada(linha + 1, coluna + 2)
                        aux = tab[linha][coluna + 1]
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux, aux)
                        tabuleiro_preenche_posicao(tabuleiro, cord_aux_2, 0)
        actualiza_pontuacao(tabuleiro, pontuacao)
        return tabuleiro
    elif movimento == 'e' or movimento == 'E':
        for ciclo in range(len(tab)):
            for linha in range(len(tab)):
                for coluna in range(len(tab[0]) - 1):
                    coluna = len(tab) - 1 - coluna
                    if tab[linha][coluna] == 0 and tab[linha][coluna - 1] != 0:
                        aux = tab[linha][coluna - 1]
                        tab[linha][coluna] = aux
                        tab[linha][coluna - 1] = 0
                        coordenada_aux = coordenada(linha + 1, coluna)
                        coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
        for linha in range(len(tab)):
            for coluna in range(len(tab[0]) - 1):
                coluna = len(tab) - 1 - coluna
                if tab[linha][coluna] == tab[linha][coluna - 1] and tab[linha][coluna - 1] != 0:
                    aux = tab[linha][coluna - 1] + tab[linha][coluna]
                    tab[linha][coluna] = aux
                    tab[linha][coluna - 1] = 0
                    coordenada_aux = coordenada(linha + 1, coluna)
                    # coordenada_aux.mostra_cord()
                    coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                    # coordenada_aux_2.mostra_cord()
                    tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                    tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
                    pontuacao += aux
        for ciclo in range(len(tab)):
            for linha in range(len(tab)):
                for coluna in range(len(tab[0]) - 1):
                    coluna = len(tab) - 1 - coluna
                    if tab[linha][coluna] == 0 and tab[linha][coluna - 1] != 0:
                        aux = tab[linha][coluna - 1]
                        tab[linha][coluna] = aux
                        tab[linha][coluna - 1] = 0
                        coordenada_aux = coordenada(linha + 1, coluna)
                        coordenada_aux_2 = coordenada(linha + 1, coluna + 1)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux_2, aux)
                        tabuleiro_preenche_posicao(tabuleiro, coordenada_aux, 0)
        actualiza_pontuacao(tabuleiro, pontuacao)
        return tabuleiro
    else:
        raise ValueError('2048: Movimento inválido.'.center(5))


# Classes:

class coordenada:
    def __init__(self, l, c):
        if l in range(1, 9) and c in range(1, 9) and isinstance(l, int) and isinstance(c, int):
            self.cord = {'l': l, 'c': c}
        else:
            raise ValueError("cria_coordenada: argumentos invalidos")

    def coordenada_linha(self):
        return self.cord['l']

    def coordenada_coluna(self):
        return self.cord['c']

    def mostra_cord(self):
        print(self.cord)

    def coordenadas_iguais(self, outro):
        if self.coordenada_coluna() == outro.coordenada_coluna() and self.coordenada_linha() == outro.coordenada_linha():
            return True
        return False


class tabuleiro:
    def __init__(self, tamanho=4, pontuacao=0, tabuleiro=None):
        if tabuleiro == None:
            tab = []
            for linha in range(tamanho):
                aux = []
                for coluna in range(tamanho):
                    aux.append(0)
                tab.append(aux)
            self.tab = tab
            self.pontuacao = pontuacao
        else:
            self.tab = [x[:] for x in tabuleiro.get_tabuleiro()]
            self.pontuacao = tabuleiro.tabuleiro_pontuacao()


    def tabuleiro_posicao(self, coord):
        if e_coordenada(coord):
            return self.tab[coord.coordenada_linha()][coord.coordenada_coluna()]
        raise ValueError('tabuleiro: A coordenada que você inseriu não é válida!!!')

    def get_tabuleiro(self):
        return self.tab

    def atualiza_posicao_tabuleiro(self, linha, coluna, valor):
        self.tab[linha][coluna] = valor

    def tabuleiro_pontuacao(self):
        return self.pontuacao

    def set_potuacao(self, valor):
        self.pontuacao += valor

    def tabuleiro_posicoes_zero(self):
        posicoes = []
        for linha in range(len(self.tab)):
            for coluna in range(len(self.tab[0])):
                if self.tab[linha][coluna] == 0:
                    posicoes.append([linha + 1, coluna + 1])
        return posicoes
