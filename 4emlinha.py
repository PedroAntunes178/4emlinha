#importes
import numpy as np
import pygame
import sys
import math
import time

#variaveis globais
#numeros magicos
NUM_COLUNAS = 7
NUM_LINHAS = 6
MEDIDA_POR_QUADRADO = 100 #isto está em pixeis
RAIO_PECA = int(MEDIDA_POR_QUADRADO/2 - 5)
# definição de cores
AZUL_NEEC = (0, 157, 224)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PECA1 = (225, 0, 0)
PECA2 = (0, 225, 225)

#esta função está a criar uma matriz de zeros, isto para simular o nosso tabuleiro com x colunas e y linhas
def criar_tabuleiro():
    tabuleiro = np.zeros((NUM_LINHAS,NUM_COLUNAS))
    return tabuleiro

#esta função serve para imprimir o tabuleiro/matriz no terminar da forma como é suposto a vermos (ou seja com o [0][0] no canto inferior esquerdo, se fizesse só print este estaria no canto superior)
def imprimir_tabuleiro(tabuleiro):
	print(np.flip(tabuleiro, 0))

#esta função vê qual é a casa da matriz em que a peça vai ficar e posiciona a peça no tabuleiro
def colocar_peca_no_tabuleiro(tabuleiro, col, player, lin):
    for linha in range(NUM_LINHAS):
        if tabuleiro[linha][col] == 0:
            tabuleiro[linha][col] = player
            return True
    return False

#esta função retorna True se for feito 4 em linha
def vitoria(tabuleiro, peca):
    # Verificacao horizontal
    for x in range(NUM_COLUNAS-3):
        for y in range(NUM_LINHAS):
            if tabuleiro[y][x] == peca and tabuleiro[y][x+1] == peca and tabuleiro[y][x+2] == peca and tabuleiro[y][x+3] == peca:
                return True
    # Verificacao vertical
    for x in range(NUM_COLUNAS):
        for y in range(NUM_LINHAS-3):
            if tabuleiro[y][x] == peca and tabuleiro[y+1][x] == peca and tabuleiro[y+2][x] == peca and tabuleiro[y+3][x] == peca:
                return True
    # Verificacao diagonal esquerda -> direita (baixo->cima)
    for x in range(NUM_COLUNAS-3):
        for y in range(NUM_LINHAS-3):
            if tabuleiro[y][x] == peca and tabuleiro[y+1][x+1] == peca and tabuleiro[y+2][x+2] == peca and tabuleiro[y+3][x+3] == peca:
                return True
    # Verificacao diagonal direita -> esquerda (cima->baixo)
    for x in range(NUM_COLUNAS-3):
        for y in range(3, NUM_LINHAS):
            if tabuleiro[y][x] == peca and tabuleiro[y-1][x+1] == peca and tabuleiro[y-2][x+2] == peca and tabuleiro[y-3][x+3] == peca:
                return True

    return False

#esta funão desenha o tabuleiro em pygame
def desenhar_tabuleiro(tabuleiro, screen, altura):
	for c in range(NUM_COLUNAS):
		for r in range(NUM_LINHAS):
			pygame.draw.rect(screen, AZUL_NEEC, (c*MEDIDA_POR_QUADRADO, r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO))
			pygame.draw.circle(screen, PRETO, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)

	for c in range(NUM_COLUNAS):
		for r in range(NUM_LINHAS):
			if tabuleiro[r][c] == 1:
				pygame.draw.circle(screen, PECA1, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), altura-int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)
			elif tabuleiro[r][c] == 2:
				pygame.draw.circle(screen, PECA2, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), altura-int(r*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO_PECA)
	pygame.display.update()

#esta função é onde vai correr o jogo
def main():
    tabuleiro = criar_tabuleiro()
    game_over = False
    vez_de = 0

    pygame.init()
    largura = NUM_COLUNAS * MEDIDA_POR_QUADRADO
    altura = (NUM_LINHAS+1) * MEDIDA_POR_QUADRADO
    tamanho = (largura, altura)
    screen = pygame.display.set_mode(tamanho)
    desenhar_tabuleiro(tabuleiro, screen, altura)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    while not(game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN :
                posx = event.pos[0]
                col = int(math.floor(posx/MEDIDA_POR_QUADRADO))
                lin = -1
                if vez_de == 0:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 1, lin)):
                        vez_de += 1
                    if vitoria(tabuleiro, 1):
                        label = myfont.render("Player 1 wins!!", 1, PECA1)
                        screen.blit(label, (40,10))
                        game_over = True
                else:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 2, lin)):
                        vez_de += 1
                    if vitoria(tabuleiro, 2):
                        label = myfont.render("Player 2 wins!!", 1, PECA2)
                        screen.blit(label, (40,10))
                        game_over = True
                vez_de += 1
                vez_de = vez_de%2
                desenhar_tabuleiro(tabuleiro, screen, altura)
                #imprimir_tabuleiro(tabuleiro)
            if game_over:
                for k in range(3):
                    pygame.draw.rect(screen, BRANCO, (int((largura-3*MEDIDA_POR_QUADRADO)/2), int((altura-MEDIDA_POR_QUADRADO)/2) , 3*MEDIDA_POR_QUADRADO, 2*MEDIDA_POR_QUADRADO))
                    time_num = myfont.render(str(3-k), 1, PRETO)
                    screen.blit(time_num, (int((largura-2*MEDIDA_POR_QUADRADO)/2),int(altura/2)))
                    pygame.display.update()
                    time.sleep(1.00)

main()