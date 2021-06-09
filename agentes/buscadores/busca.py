from agentes.problemas.eightpuzzle import ProblemaEightPuzzle
from copy import deepcopy
import time, heapq

from typing import Any, Optional
from dataclasses import dataclass

from agentes.tipos import TiposAgentes

class ProblemaSemSolucaoException(Exception):
    pass


@dataclass
class No():
    estado: Any
    acao: Optional[Any] = None
    custo_solucao: int = 0
    pai: Optional['No'] = None

    def calcular_profundidade(self):
        raiz = not self.pai
        return 0 if raiz else self.pai.calcular_profundidade() + 1
    
    def caminho_acoes(self) -> list:
        """Retorna uma lista com as ações em ordem para atingir o estado
        que este nó armazena.
        """
        raiz = not self.pai
        return [] if raiz else self.pai.caminho_acoes() + [self.acao]

    @classmethod
    def criar_no_filho(cls, problema, pai, acao):
        novo_estado = problema.resultado(pai.estado, acao)
        custo_solucao = pai.custo_solucao + problema.custo()
        return cls(novo_estado, acao, custo_solucao, pai)
    
    def __repr__(self) -> str:
        return f'No({self.estado!r},{self.acao!r})'


def busca_arvore(problema, tipo_agente) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial())]
    visited = list()
    while borda:
        if tipo_agente == TiposAgentes.AUTO_BFS:
            folha = borda.pop(0)
        else:
            folha = borda.pop()

        if folha.estado.tabuleiro not in visited: 
            visited.append(folha.estado.tabuleiro)
            if problema.teste_objetivo(folha.estado.tabuleiro):
                return folha

            for acao in problema.acoes(folha.estado):
                expandido = No.criar_no_filho(problema, folha, acao)
                borda.append(expandido)
                
            print(f'Jogadas processadas: {len(visited)}')

    raise ProblemaSemSolucaoException()

def busca_heuristica(problema, tipo_agente) -> No:
    fila = list()

    estado_inicial = problema.estado_inicial()
    contador = 0
    custo_acumulado = 0
    valor_f = problema.funcao_avaliacao(estado_inicial.tabuleiro, custo_acumulado)
    heapq.heappush(fila, [valor_f, contador, No(estado_inicial)])

    visited = list()
    while fila:
        folha = heapq.heappop(fila)
        valor_f = folha[0]
        no_atual = folha[2]

        if no_atual.estado.tabuleiro not in visited:
            visited.append(no_atual.estado.tabuleiro)

            if problema.funcao_heuristica(no_atual.estado.tabuleiro) == 0:
                return no_atual
            
            for acao in problema.acoes(no_atual.estado):
                contador += 1
                no_filho = No.criar_no_filho(problema, no_atual, acao)
                
                if tipo_agente == TiposAgentes.H_ASTAR and custo_acumulado != no_filho.custo_solucao:
                    custo_acumulado = no_filho.custo_solucao

                valor_f_filho = problema.funcao_avaliacao(no_filho.estado.tabuleiro, custo_acumulado)
                heapq.heappush(fila, [valor_f_filho, contador, no_filho])
            
        print(f'Jogadas processadas: {len(visited)}')
        
