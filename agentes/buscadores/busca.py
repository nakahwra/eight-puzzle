import time

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
