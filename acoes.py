from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    MOVER = 'mover'
    
class DirecaoMover(Enum):
    DIREITA = 'Direita'
    ESQUERDA = 'Esquerda'
    CIMA = 'Cima'
    BAIXO = 'Baixo'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: str
    
    @classmethod
    def mover(cls, direcao: DirecaoMover) -> 'AcaoJogador':
        return cls(AcoesJogador.MOVER, direcao)