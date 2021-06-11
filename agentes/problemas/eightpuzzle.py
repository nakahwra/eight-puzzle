import copy

from typing import Sequence, Set, List
from dataclasses import dataclass


@dataclass
class PosicaoVazia():
    x: int
    y: int


@dataclass
class EstadoEightPuzzle():
    tabuleiro: List
    posicao_vazia: PosicaoVazia


@dataclass
class Mover():
    direcao: str


class ProblemaEightPuzzle():

    def __init__(self, percepcao_mundo) -> None:
        super().__init__()

        self.percepcao_mundo = percepcao_mundo

    def estado_inicial(self):
        x, y = self.percepcao_mundo.posicao_vazia
        return EstadoEightPuzzle(self.percepcao_mundo.tabuleiro, PosicaoVazia(x, y))

    @staticmethod
    def acoes(estado: EstadoEightPuzzle):
        acoes_possiveis = list()
        tabuleiro = estado.tabuleiro
        x, y = estado.posicao_vazia.x, estado.posicao_vazia.y

        if (y-1) <= 2 and (y-1) >= 0:
            acoes_possiveis.append(Mover('esquerda'))

        if (y+1) <= 2 and (y+1) >= 0:
            acoes_possiveis.append(Mover('direita'))

        if (x-1) <= 2 and (x-1) >= 0:
            acoes_possiveis.append(Mover('cima'))

        if (x+1) <= 2 and (x+1) >= 0:
            acoes_possiveis.append(Mover('baixo'))

        return acoes_possiveis

    @staticmethod
    def resultado(estado: EstadoEightPuzzle, acao: Mover):
        acoes_possiveis = ProblemaEightPuzzle.acoes(estado)

        if acao not in acoes_possiveis:
            raise ValueError("Ação inválida!")

        tabuleiro = copy.deepcopy(estado.tabuleiro)
        x, y = estado.posicao_vazia.x, estado.posicao_vazia.y

        if acao.direcao == 'esquerda':
            tabuleiro[x][y], tabuleiro[x][y-1] = tabuleiro[x][y-1], tabuleiro[x][y]

        elif acao.direcao == 'direita':
            tabuleiro[x][y], tabuleiro[x][y+1] = tabuleiro[x][y+1], tabuleiro[x][y]

        elif acao.direcao == 'cima':
            tabuleiro[x][y], tabuleiro[x-1][y] = tabuleiro[x-1][y], tabuleiro[x][y]

        elif acao.direcao == 'baixo':
            tabuleiro[x][y], tabuleiro[x+1][y] = tabuleiro[x+1][y], tabuleiro[x][y]
        
        x, y = ProblemaEightPuzzle.get_posicao_vazia(tabuleiro)
        return EstadoEightPuzzle(tabuleiro, PosicaoVazia(x,y))

    @staticmethod
    def teste_objetivo(tabuleiro) -> bool:
        parse_tabuleiro = ProblemaEightPuzzle.parse_tabuleiro(tabuleiro)
        solucao = ProblemaEightPuzzle.get_solucao()
        return parse_tabuleiro == solucao
    
    @staticmethod
    def custo() -> int:
        ''' Custo uniforme de valor 1 (um) para todas as jogadas
        '''
        return 1
    
    @staticmethod
    def get_posicao_vazia(tabuleiro):
        for linha in range(len(tabuleiro)):
            for coluna in range(len(tabuleiro[linha])):
                if tabuleiro[linha][coluna] == 0:
                    return linha, coluna
    
    @staticmethod
    def funcao_avaliacao(tabuleiro, custo_acumulado):
        return ProblemaEightPuzzle.funcao_heuristica2(tabuleiro) + custo_acumulado

    @staticmethod
    def funcao_heuristica(tabuleiro):
        incorretos = 0
        tabuleiro = ProblemaEightPuzzle.parse_tabuleiro(tabuleiro)
        solucao = ProblemaEightPuzzle.get_solucao()
        for i in tabuleiro:
            if tabuleiro[i] != solucao[i]:
                incorretos += 1
        return incorretos

    @staticmethod
    def funcao_heuristica2(tabuleiro):
        tamanho_tabuleiro = len(tabuleiro)
        resultado, contador = 0, 1
        for i in range(0, tamanho_tabuleiro):
            for j in range(0, tamanho_tabuleiro):
                index = tabuleiro[i][j] - 1
                if index == -1:
                    distancia = (2 - i) + (2 - j)
                else:
                    distancia = abs(i - (index / tamanho_tabuleiro)) + abs(j - (index % tamanho_tabuleiro))
                resultado += distancia
                contador += 1
        return resultado

    @staticmethod
    def get_solucao():
        return [1,2,3,4,5,6,7,8,0]

    @staticmethod
    def parse_tabuleiro(tabuleiro):
        parse_tabuleiro = list()
        for linha in tabuleiro:
            for coluna in linha:
                parse_tabuleiro.append(coluna)
        
        return parse_tabuleiro
