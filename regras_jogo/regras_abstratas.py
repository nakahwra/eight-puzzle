from abc import ABC, abstractmethod

class AbstractRegrasJogo(ABC):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """

    @abstractmethod
    def registrarPersonagemJogador(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return
    
    @abstractmethod
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return

    @abstractmethod
    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return

    @abstractmethod
    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        return
    
    @abstractmethod
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        return
    
    @abstractmethod
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

def construir_jogo(*args,**kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return NomeDoSeuJogo()
