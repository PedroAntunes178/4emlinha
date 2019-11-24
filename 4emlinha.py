#importes
import numpy as np
import pygame
import sys
import math

#variaveis globais
#numeros magicos
NUM_COLUNAS = 7
NUM_LINHAS = 6
MEDIDA_POR_QUADRADO = 100 #isto está em pixeis
RAIO_PECA = int(MEDIDA_POR_QUADRADO/2 - 5)
#cores
AZUL_NEEC = (0, 157, 224)
PRETO = (0, 0, 0)
PECA1 = (225, 0, 0)
PECA2 = (0, 225, 225)

#esta função está a criar uma matriz de zeros, isto para simular o nosso tabuleiro com x colunas e y linhas
def criar_tabuleiro():
    tabuleiro = np.zeros((NUM_LINHAS,NUM_COLUNAS))
    return tabuleiro

#esta função serve para imprimir o tabuleiro/matriz no terminar da forma como é suposto a vermos (ou seja com o [0][0] no canto inferior esquerdo, se fizesse só print este estaria no canto superior)
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

#esta funão desenha o tabuleiro em pygame
def desenhar_tabuleiro(tabuleiro, screen):
	for c in range(NUM_COLUNAS):
		for r in range(NUM_LINHAS):
			pygame.draw.rect(screen, AZUL_NEEC, (c*MEDIDA_POR_QUADRADO, r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO))
			pygame.draw.circle(screen, PRETO, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)

	for c in range(NUM_COLUNAS):
		for r in range(NUM_LINHAS):
			if tabuleiro[r][c] == 1:
				pygame.draw.circle(screen, PECA1, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), height-int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)
			elif tabuleiro[r][c] == 2:
				pygame.draw.circle(screen, PECA2, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), height-int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)
	pygame.display.update()

#esta função é onde vai correr o jogo
def main():
    tabuleiro = criar_tabuleiro()
    game_over = False
    vez_de = 0

    pygame.init()
    width = NUM_COLUNAS * MEDIDA_POR_QUADRADO
    height = (NUM_LINHAS+1) * MEDIDA_POR_QUADRADO
    size = (width, height)
    screen = pygame.display.set_mode(size)
    desenhar_tabuleiro(tabuleiro, screen)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    while not(game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN :
                posx = event.pos[0]
                col = int(math.floor(posx/MEDIDA_POR_QUADRADO))
                if vez_de == 0:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 1)):
                        vez_de += 1
                    if vitoria(tabuleiro):
                        label = myfont.render("Player 1 wins!!", 1, PECA1)
                        screen.blit(label, (40,10))
                        game_over = True
                else:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 2)):
                        vez_de += 1
                    if vitoria(tabuleiro):
                        label = myfont.render("Player 2 wins!!", 1, PECA2)
                        screen.blit(label, (40,10))
                        game_over = True
                vez_de += 1
                vez_de = vez_de%2
                desenhar_tabuleiro(tabuleiro, screen)
                imprimir_tabuleiro(tabuleiro)


main()
