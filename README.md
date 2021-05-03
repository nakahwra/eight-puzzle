# 🕹 Eight Puzzle CLI
Jogo do quebra-cabeças de 8 peças em linha de comando desenvolvido para a disciplina de Inteligência Artificial. Escrito em python, este projeto tem como objetivo a aplicação dos conceitos estudados e a implementação de um simples agente inteligente que consiga resolver o jogo.

## Execução do projeto
### Dependências
- Python 3.9.0 ou superior
### Execução
- Clone o projeto (ou baixe):
  ```shell
  git clone https://github.com/Nakahwra/EightPuzzle.git
  && cd EightPuzzle/
  ```
 - Execute o arquivo principal ```jogo.py```:
    ```shell
    python3 ./jogo.py
    ```
    
## Agentes automáticos
São implementados dois agentes automáticos que utilizam dois algoritmos de buscas de "força bruta":

### Breadth-first Search Algorithm - BFS
Busca em largura, algoritmo de busca em grafos/árvores onde prioriza-se a exploração de todos os vértices vizinhos antes da travessia para a próxima profundidade, até que se encontre um nó solução.  
![bfs](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif)

### Depth-first Search Algorithm - DFS
Busca em profundidade, algoritmo de busca em grafos/árvores onde prioriza-se a exploração de um dos ramos do nó raíz em sua totalidade até que se encontre um nó solução.  
![dfs](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

## Configurações opcionais
#### Tabuleiro
O tabuleiro pode ser ajustado no construtor da classe de regras do jogo em: ```regras_jogo/regras_eightpuzzle.py```. Lá estão disponíveis outros dois tabuleiros usados para testes, e também pode-se configurar novos tabuleiros.
#### Intervalo entre jogadas
O intervalo entre cada jogada de um agente automático pode ser configurado alterando o parâmetro da função ```sleep``` em ```agentes/agente_automatico.py``` no método ```escolherProximaAcao```

---
🚀 Desenvolvido por **Lucas Nakahara** e **Gabriel Rodrigues**
