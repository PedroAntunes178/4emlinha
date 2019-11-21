import numpy as np

NUM_COLUNAS = 8
NUM_LINHAS = 10

def criar_tabuleiro():
    tabuleiro = np.zeros((NUM_LINHAS,NUM_COLUNAS))
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
	print(np.flip(tabuleiro, 0))

tabuleiro = criar_tabuleiro()
game_over = False
jogador = 0
