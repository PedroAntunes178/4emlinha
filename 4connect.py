#imports
import numpy as np
import pygame
import sys
import math

#variaveis globais
#numeros magicos
NUM_COLUNAS = 7
NUM_LINHAS = 6
MEDIDA_POR_QUADRADO = 100 #em pixeis
RAIO_PECA = int(MEDIDA_POR_QUADRADO/2 - 5)

#cores
AZUL_NEEC = (0, 157, 224)
PRETO = (0, 0, 0)
PECA1 = (225, 0, 0)
PECA2 = (0, 225, 225)

#esta função cria uma matriz de zeros, neste caso é o nosso tabuleiro com x colunas e y linhas
def criar_tabuleiro():
	tabuleiro = np.zeros((NUM_LINHAS,NUM_COLUNAS))
	return tabuleiro

#esta função serve para imprimir o tabuleiro/matriz no terminal (com o [0][0] no canto inferior esquerdo, se fizesse só print este estaria no canto superior)????
def imprimir_tabuleiro(tabuleiro):
	print(np.flip(tabuleiro, 0))

#esta função verifica se a coluna selecionada tem espaço para colocar a peça
#def coluna_cheia(tabuleiro, col):
#    if tabuleiro[0][col] == 0:
#        return False
#    else:
#        return True

#esta função vê qual é a casa da matriz em que a peça vai ficar e posiciona a peça no tabuleiro
def colocar_peca_no_tabuleiro(tabuleiro, col, player):
    for linha in range(NUM_LINHAS):
        if tabuleiro[linha][col] == 0:
            tabuleiro[linha][col] = player
            return True
    return False

#esta função retorna True se for feito 4 em linha
def vitoria(tabuleiro):
    return False


#esta função é onde vai correr o jogo
def main():
    tabuleiro = criar_tabuleiro()
    game_over = False
    vez_de = 0

    while not(game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN :
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if vez_de == 0:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 1)):
                        vez_de += 1
                    if verifica(tabuleiro):
                        label = myfont.render("Player 1 wins!!", 1, PECA1)
                        screen.blit(label, (40,10))
                        game_over = True
                else:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 2)):
                        vez_de += 1
                    if verifica(tabuleiro):
                        label = myfont.render("Player 2 wins!!", 1, PECA2)
                        screen.blit(label, (40,10))
                        game_over = True
                vez_de += 1
                vez_de = vez_de%2
                desenhar_tabuleiro(tabuleiro, screen)
                imprimir_tabuleiro(tabuleiro)


main()
