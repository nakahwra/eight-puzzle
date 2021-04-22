from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    NOME_DE_UMA_ACAO_VALIDA_NO_SEU_JOGO = 'nome_de_uma_acao_valida_no_seu_jogo'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def nome_de_uma_acao_valida_no_seu_jogo(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.NOME_DE_UMA_ACAO_VALIDA_NO_SEU_JOGO, (p1,p2,p3,p4))