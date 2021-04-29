from .humano import AgentePrepostoESHumano
from .auto_bfs import AgenteAutomaticoBfs
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    if tipo_agente == TiposAgentes.AUTO_BFS:
        return AgenteAutomaticoBfs()
    
    raise ValueError("Não foi escolhido nenhum tipo de agente válido.")