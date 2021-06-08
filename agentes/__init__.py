from .humano import AgentePrepostoESHumano
from .agente_automatico import AgenteAutomatico
from .agente_heuristico import AgenteHeuristico
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    elif tipo_agente == TiposAgentes.AUTO_BFS or tipo_agente == TiposAgentes.AUTO_DFS:
        return AgenteAutomatico(tipo_agente)
    else:
        return AgenteHeuristico(tipo_agente)
    
    raise ValueError("Não foi escolhido nenhum tipo de agente válido.")
