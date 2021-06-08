#!/usr/bin/env python3

import time

from regras_jogo.regras_eightpuzzle import construir_jogo
from regras_jogo.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se atégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def escolher_agente():
    agente_escolhido = None

    while not agente_escolhido:
        print("-> Escolha o tipo de agente <-")
        print("1. Humano")
        print("2. Agente BFS")
        print("3. Agente DFS")
        print("4. Agente Guloso")
        print("5. Agente A*")
        tipo_agente = str(input('Insira um número: '))

        agentes = {
            '1': TiposAgentes.PREPOSTO_HUMANO,
            '2': TiposAgentes.AUTO_BFS,
            '3': TiposAgentes.AUTO_DFS,
            '4': TiposAgentes.H_GREEDY,
            '5': TiposAgentes.H_ASTAR,
        }

        agente_escolhido = agentes.get(tipo_agente)

        if not agente_escolhido:
            print('*** Agente inválido ***\n')

    return agente_escolhido


def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarPersonagemJogador(Personagens.JOGADOR_EIGHT_PUZZLE)
    agente_escolhido = escolher_agente()
    agente_jogador = construir_agente(agente_escolhido, Personagens.JOGADOR_EIGHT_PUZZLE)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        jogo.atualizarEstado(1)
        tempo_de_jogo += 1

    jogo.terminarJogo()
    ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
    agente_jogador.adquirirPercepcao(ambiente_perceptivel)


if __name__ == '__main__':
    iniciar_jogo()