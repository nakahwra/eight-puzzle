import time

from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMover

from .abstrato import AgenteAbstrato
from .problemas.eightpuzzle import ProblemaEightPuzzle
from .buscadores.busca import busca_arvore_bfs

class AgenteAutomaticoBfs(AgenteAbstrato):

    def __init__(self) -> None:
        super().__init__()

        self.problema: ProblemaEightPuzzle = None
        self.solucao: list = None
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        AgenteAutomaticoBfs.desenhar_tabuleiro(percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaEightPuzzle(percepcao_mundo)
    
    def escolherProximaAcao(self):
        if not self.solucao:
            no_solucao = busca_arvore_bfs(self.problema)
            self.solucao = no_solucao.caminho_acoes()
            # print(len(self.solucao), self.solucao)
            if not self.solucao:
                raise Exception("Agente BFS não encontrou solução.")
        
        acao = self.solucao.pop(0)
        print(f"Próxima ação é {acao}.")
        time.sleep(2)

        direcao = AgenteAutomaticoBfs.traduzir_acao_jogo(acao)
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
        print("-" * 48)
        for x in percepcao_mundo.tabuleiro:
            print(x)

        if percepcao_mundo.mensagem_jogo:
            print(f'\nMensagem do jogo: {percepcao_mundo.mensagem_jogo}')
