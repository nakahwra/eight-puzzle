from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'
    H_GREEDY = 'Automático Guloso'
    H_ASTAR  = 'Automático A*'
    
    # adicionar outros tipos de agentes de acordo com o necessário
