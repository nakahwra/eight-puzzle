import time

from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMover

from .abstrato import AgenteAbstrato
from .problemas.eightpuzzle import ProblemaEightPuzzle
from .buscadores.busca import busca_arvore

class AgenteAutomatico(AgenteAbstrato):

    def __init__(self, tipo_agente) -> None:
        super().__init__()

        self.problema: ProblemaEightPuzzle = None
        self.solucao: list = None
        self.tipo_agente = tipo_agente
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        AgenteAutomatico.desenhar_tabuleiro(percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaEightPuzzle(percepcao_mundo)
    
    def escolherProximaAcao(self):
        if not self.solucao:
            no_solucao = busca_arvore(self.problema, self.tipo_agente)
            self.solucao = no_solucao.caminho_acoes()
            if not self.solucao:
                raise Exception(f'Agente {self.tipo_agente.value} não encontrou solução.')
        
        acao = self.solucao.pop(0)
        print(f'\nPróxima ação é mover para "{acao.direcao}".')
        time.sleep(1)

        direcao = AgenteAutomatico.traduzir_acao_jogo(acao)
        return AcaoJogador.mover(direcao)

    @staticmethod
    def traduzir_acao_jogo(acao) :
        direcoes = {
            'esquerda': DirecaoMover.ESQUERDA,
            'direita': DirecaoMover.DIREITA,
            'cima': DirecaoMover.CIMA,
            'baixo': DirecaoMover.BAIXO
        }

        direcao = direcoes.get(acao.direcao)
        if not direcao:
            raise ValueError()
        
        return direcao

    @staticmethod
    def desenhar_tabuleiro(percepcao_mundo: PercepcoesJogador):
        print("-" * 42)
        for x in percepcao_mundo.tabuleiro:
            print(x)

        if percepcao_mundo.mensagem_jogo:
            print(f'\nMensagem do jogo: {percepcao_mundo.mensagem_jogo}')
