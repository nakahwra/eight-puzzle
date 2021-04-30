from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, DirecaoMover

class RegrasEightPuzzle(AbstractRegrasJogo):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """

    def __init__(self):
        super().__init__()
        # Tabuleiro Padrão - resolvível por apenas BFS em tempo razoável
        tabuleiro_completo = [
            [0,1,2],
            [5,6,3],
            [4,7,8],
        ]
        
        # Tabuleiro Teste 1 - resolvível para BFS e DFS em tempo razoável
        # tabuleiro_completo = [
        #     [1,2,3],
        #     [4,5,6],
        #     [7,0,8],
        # ]

        # Tabuleiro Teste 2 - aparentemente não-resolvível por agentes auto. em tempo razoável
        # tabuleiro_completo = [
        #     [7,2,4],
        #     [5,0,6],
        #     [8,3,1],
        # ]

        self.tabuleiro = tabuleiro_completo
        self.id_personagens = {Personagens.JOGADOR_EIGHT_PUZZLE: 0}
        self.acoes_personagens = {0: None}
        self.posicao_vazia = self.descobrir_posicao_vazia()
        self.msg_jogador = None

    def registrarPersonagemJogador(self, personagem):
        """ Cria ou recupera id de um personagem.
        """
        return self.id_personagens[personagem]
    
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        tabuleiro = list()
        for linha in self.tabuleiro:
            for coluna in linha:
                tabuleiro.append(coluna)

        solucao = [1,2,3,4,5,6,7,8,0]
        return tabuleiro == solucao

    def gerarCampoVisao(self, id_personagem):
        """ Retorna um PercepcoesJogador para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        PercepcoesJogador é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        percepcoes_jogador = PercepcoesJogador(
            tabuleiro = self.tabuleiro,
            dimensoes = (3, 3),
            mensagem_jogo = self.msg_jogador,
            posicao_vazia = self.posicao_vazia
        )

        self.msg_jogador = None
        return percepcoes_jogador

    def registrarProximaAcao(self, id_personagem, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acoes_personagens[id_personagem] = acao
    
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acoes_personagens[self.id_personagens[Personagens.JOGADOR_EIGHT_PUZZLE]]

        if acao_jogador.tipo == AcoesJogador.MOVER:
            direcao = acao_jogador.parametros
            direcoes_validas = self.get_direcoes_validas()

            if direcao in direcoes_validas:
                x,y = self.posicao_vazia
                if direcao == DirecaoMover.ESQUERDA:
                    self.tabuleiro[x][y], self.tabuleiro[x][y-1] = self.tabuleiro[x][y-1], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.DIREITA:
                    self.tabuleiro[x][y], self.tabuleiro[x][y+1] = self.tabuleiro[x][y+1], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.CIMA:
                    self.tabuleiro[x][y], self.tabuleiro[x-1][y] = self.tabuleiro[x-1][y], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.BAIXO:
                    self.tabuleiro[x][y], self.tabuleiro[x+1][y] = self.tabuleiro[x+1][y], self.tabuleiro[x][y]
            else:
                self.msg_jogador = 'Direção é inválida'
                
            self.posicao_vazia = self.descobrir_posicao_vazia()
        return
    
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        self.msg_jogador = 'Parabéns, você venceu!'
    
    def get_direcoes_validas(self):
        direcoes_validas = list()
        x, y = self.posicao_vazia

        if (y-1) <= 2 and (y-1) >= 0:
            direcoes_validas.append(DirecaoMover.ESQUERDA)
        if (y+1) <= 2 and (y+1) >= 0:
            direcoes_validas.append(DirecaoMover.DIREITA)
        if (x-1) <= 2 and (x-1) >= 0:
            direcoes_validas.append(DirecaoMover.CIMA)
        if (x+1) <= 2 and (x+1) >= 0:
            direcoes_validas.append(DirecaoMover.BAIXO)

        return direcoes_validas

    def descobrir_posicao_vazia(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 0:
                    return (i, j)


def construir_jogo(*args,**kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasEightPuzzle()
