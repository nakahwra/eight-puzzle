from agentes.abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMover

class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        print("-" * 48)
        for x in percepcao_mundo.tabuleiro:
            print(x)

        if percepcao_mundo.mensagem_jogo:
            print(f'\nMensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def escolherProximaAcao(self):
        jogada = None
        while not jogada:
            jogada = input("\nEscreva a direção que deseja mover (e,d,c,b): ").strip()
            try:                
                direcao = AgentePrepostoESHumano.parse_jogada(jogada)            
            except ValueError:
                jogada = None
                print("Jogada entrada é inválida. Tente novamente.")

        return AcaoJogador.mover(direcao)

    @staticmethod
    def parse_jogada(d: str) :
        direcoes = {
            'e': DirecaoMover.ESQUERDA,
            'd': DirecaoMover.DIREITA,
            'c': DirecaoMover.CIMA,
            'b': DirecaoMover.BAIXO
        }

        direcao = direcoes.get(d.lower())
        if not direcao:
            raise ValueError()
        
        return direcao
