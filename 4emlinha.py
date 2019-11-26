#imports
import numpy as np
import pygame
import sys
import math

#variaveis globais
#numeros magicos
NUM_COLUNAS = 7
NUM_LINHAS = 7
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
	print('')

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
            return linha
    return -1

#esta função retorna True se for feito 4 em linha
def verifica(tabuleiro, linha, coluna):
    h = 1
    d = 1
    x = 1
    try:
        if(tabuleiro[linha][coluna] == tabuleiro[linha-1][coluna] == tabuleiro[linha-2][coluna] == tabuleiro[linha-3][coluna]):
            return True
    except: 
        pass

   
    try: 
        for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha][coluna-x]):
                h = h+1
                print ('1:',h)
                if(h == 4):
                    return True;
        for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha][coluna+x]):
                    h = h+1
                    print ('1b:',h)
                    if(h == 4):
                        return True;
    except:
        pass
    try:
         for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha-x][coluna-x]):
                d = d+1
                print ('d1:',d)
                if(d == 4):
                    return True;
         for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha+x][coluna+x]):
                d = d+1
                print ('d1.:',d)
                if(d == 4):
                    return True;
         for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha-x][coluna+x]):
                d = d+1
                print ('d2.:',d)
                if(d == 4):
                    return True;
         for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha+x][coluna-x]):
                d = d+1
                print ('d2..:',d)
                if(d == 4):
                    return True;
    except:
        pass
            
  

#esta função desenha o tabuleiro em pygame
def desenhar_tabuleiro(tabuleiro, screen, height):
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
    desenhar_tabuleiro(tabuleiro, screen, height)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    while not(game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                posx = event.pos[0]
                col = int(math.floor(posx/MEDIDA_POR_QUADRADO))
                if vez_de == 0:
                    linha = colocar_peca_no_tabuleiro(tabuleiro , col, 1)
                        #vez_de += 1
                    if verifica(tabuleiro.astype(int), linha, col):
                        label = myfont.render("Player 1 wins!!", 1, PECA1)
                        screen.blit(label, (40,10))
                else:
                    linha = colocar_peca_no_tabuleiro(tabuleiro, col, 2)
                        #vez_de += 1
                    if verifica(tabuleiro.astype(int), linha, col):
                        label = myfont.render("Player 2 wins!!", 1, PECA2)
                        screen.blit(label, (40,10))
                vez_de += 1
                vez_de = vez_de%2
                desenhar_tabuleiro(tabuleiro, screen, height)
                imprimir_tabuleiro(tabuleiro)


main()
