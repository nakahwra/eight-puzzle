from typing import Any, Optional
from dataclasses import dataclass

import time


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


def busca_arvore_bfs(problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial())]
    visited = list()
    while borda:
        folha = borda.pop(0)
        print(f'Jogadas processadas: {len(visited)}')
        if folha.estado.tabuleiro not in visited: 
            visited.append(folha.estado.tabuleiro)
            # print(f"Altura {folha.calcular_profundidade()}, com {len(borda)} nós na borda.")
            if problema.teste_objetivo(folha.estado.tabuleiro):
                return folha

            # print(f'Não era objetivo. Ações adjacentes são {problema.acoes(folha.estado)}.')
            for acao in problema.acoes(folha.estado):
                expandido = No.criar_no_filho(problema, folha, acao)
                borda.append(expandido)

                # print(f'Enfileirado {expandido}')
                # time.sleep(5)

    raise ProblemaSemSolucaoException()
