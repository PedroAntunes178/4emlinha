# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:52:54 2019

@author: Mariana
"""

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
RAIO = int(MEDIDA_POR_QUADRADO/2 - 5)
# definição de cores
AZUL_NEEC = (0, 157, 224)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PECA1 = (225, 0, 0)
PECA2 = (0, 225, 225)
VERDE = (0, 255, 0)
ROXO = (255, 0, 255)
CINZENTO = (150,150,150)

#esta função está a criar uma matriz de zeros, isto para simular o nosso tabuleiro com x colunas e y linhas
def criar_tabuleiro():
    tabuleiro = np.zeros((NUM_LINHAS,NUM_COLUNAS))
    return tabuleiro

#esta função serve para imprimir o tabuleiro/matriz no terminar da forma como é suposto a vermos (ou seja com o [0][0] no canto inferior esquerdo, se fizesse só print este estaria no canto superior)
def imprimir_tabuleiro(tabuleiro):
    print(np.flip(tabuleiro, 0))

#esta função vê qual é a casa da matriz em que a peça vai ficar e posiciona a peça no tabuleiro
def colocar_peca_no_tabuleiro(tabuleiro, col, player, linha):
    for linha[0] in range(NUM_LINHAS):
        if tabuleiro[linha[0]][col] == 0:
            tabuleiro[linha[0]][col] = player
            return True
    return False


#esta função retorna True se for feito 4 em linha
def vitoria(tabuleiro, linha, coluna):
    h = 1
    d1 = 1
    d2 = 1
    try:
        if(tabuleiro[linha][coluna] == tabuleiro[linha-1][coluna] == tabuleiro[linha-2][coluna] == tabuleiro[linha-3][coluna]):
            return True
    except:
        pass
    try:
        for x in [1,2,3]:
            if coluna-x >= 0:
                if(tabuleiro[linha][coluna] == tabuleiro[linha][coluna-x]):
                    h = h+1
                    #print('1:',h)
                    if(h == 4):
                        return True
                else:
                    break
            else:
                break
        for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha][coluna+x]):
                h = h+1
                #print ('1b:',h)
                if(h == 4):
                    return True
            else:
                break
    except:
        pass
    try:
        for x in [1,2,3]:
            if linha-x or coluna-x:
                if(tabuleiro[linha][coluna] == tabuleiro[linha-x][coluna-x]):
                    d1 = d1+1
                    #print('d1:',d1)
                    if(d1 == 4):
                        return True
                else:
                    break
            else:
                break
        for x in [1,2,3]:
            if(tabuleiro[linha][coluna] == tabuleiro[linha+x][coluna+x]):
                d1 = d1+1
                #print ('d1.:',d1)
                if(d1 == 4):
                    return True
            else:
                break
    except:
        pass

    try:
        for x in [1,2,3]:
            if linha-x >= 0:
                if(tabuleiro[linha][coluna] == tabuleiro[linha-x][coluna+x]):
                    d2 = d2+1
                    #print('d2.:',d2)
                    if(d2 == 4):
                        return True
                else:
                    break
            else:
                break
        for x in [1,2,3]:
            if coluna-x >=0:
                if(tabuleiro[linha][coluna] == tabuleiro[linha+x][coluna-x]):
                    d2 = d2+1
                    #print('d2..:',d2)
                    if(d2 == 4):
                        return True
                else:
                    break
            else:
                break
    except:
        pass
    return False

#esta funão desenha o tabuleiro em pygame
def desenhar_tabuleiro(tabuleiro, janela, altura):
    for c in range(NUM_COLUNAS):
        for l in range(NUM_LINHAS):
            pygame.draw.rect(janela, AZUL_NEEC, (c*MEDIDA_POR_QUADRADO, (l+1)*MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO))
            pygame.draw.circle(janela, PRETO, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), int(l*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO)

    for c in range(NUM_COLUNAS):
        for l in range(NUM_LINHAS):
            if tabuleiro[l][c] == 1:
                pygame.draw.circle(janela, PECA1, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), altura-int(l*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO)
            elif tabuleiro[l][c] == 2:
                pygame.draw.circle(janela, PECA2, (int(c*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2), altura-int(l*MEDIDA_POR_QUADRADO+MEDIDA_POR_QUADRADO/2)), RAIO)

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
    janela = pygame.display.set_mode(tamanho)
    desenhar_tabuleiro(tabuleiro, janela, altura)
    myfont = pygame.font.SysFont("monospace", 75)

    while not(game_over):
        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                sys.exit()

            if event.type == pygame.MOUSEMOTION :
                posx = event.pos[0]
                pygame.draw.rect(janela, PRETO, (0, 0, largura, MEDIDA_POR_QUADRADO))
                if vez_de == 0:
                    pygame.draw.circle(janela, PECA1, (posx, int(MEDIDA_POR_QUADRADO/2)), RAIO)
                else:
                    pygame.draw.circle(janela, PECA2, (posx, int(MEDIDA_POR_QUADRADO/2)), RAIO)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN :
                posx = event.pos[0]
                col = int(math.floor(posx/MEDIDA_POR_QUADRADO))
                linha = [0]
                if vez_de == 0:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 1, linha)):
                        vez_de += 1
                    elif vitoria(tabuleiro, linha[0], col):
                        pygame.draw.rect(janela, PRETO, (0, 0, largura, MEDIDA_POR_QUADRADO))
                        label = myfont.render("Player 1 wins!!", 1, PECA1)
                        janela.blit(label, (40,10))
                        game_over = True
                    else:
                        pygame.draw.circle(janela, PECA2, (posx, int(MEDIDA_POR_QUADRADO/2)), RAIO)
                else:
                    if not(colocar_peca_no_tabuleiro(tabuleiro, col, 2, linha)):
                        vez_de += 1
                    elif vitoria(tabuleiro, linha[0], col):
                        pygame.draw.rect(janela, PRETO, (0, 0, largura, MEDIDA_POR_QUADRADO))
                        label = myfont.render("Player 2 wins!!", 1, PECA2)
                        janela.blit(label, (40,10))
                        game_over = True
                    else:
                        pygame.draw.circle(janela, PECA1, (posx, int(MEDIDA_POR_QUADRADO/2)), RAIO)
                vez_de += 1
                vez_de = vez_de%2
                desenhar_tabuleiro(tabuleiro, janela, altura)
                #imprimir_tabuleiro(tabuleiro)

        if game_over:
            time.sleep(1)
            time_start = time.time()
            #print(time_start)
            pygame.draw.rect(janela, PRETO, (int((largura-5*MEDIDA_POR_QUADRADO)/2), int((altura-MEDIDA_POR_QUADRADO)/2), 5*MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO))
            pygame.draw.rect(janela, BRANCO, (int((largura-5*MEDIDA_POR_QUADRADO)/2)+4, int((altura-MEDIDA_POR_QUADRADO)/2)+4, 5*MEDIDA_POR_QUADRADO-8, MEDIDA_POR_QUADRADO-8))
            label = myfont.render("Restart!", 1, PRETO)
            janela.blit(label, (int((largura-3*MEDIDA_POR_QUADRADO)/2)+2, int((largura-3*MEDIDA_POR_QUADRADO)/2+MEDIDA_POR_QUADRADO)+2))
            while time.time() < time_start+5:
                k = int(math.floor(6-(time.time()-time_start)))
                pygame.draw.rect(janela, BRANCO, (int((largura-5*MEDIDA_POR_QUADRADO)/2), int((altura+MEDIDA_POR_QUADRADO)/2) , 5*MEDIDA_POR_QUADRADO, MEDIDA_POR_QUADRADO))
                time_str = myfont.render(str(k), 1, PRETO)
                janela.blit(time_str, (int(largura/2),int((altura+MEDIDA_POR_QUADRADO)/2)))
                for event in pygame.event.get() :
                    if event.type == pygame.MOUSEMOTION :
                        pos = pygame.mouse.get_pos()
                        if int((largura-5*MEDIDA_POR_QUADRADO)/2) < pos[0] and int((altura-MEDIDA_POR_QUADRADO)/2) < pos[1] and pos[0] < int((largura+5*MEDIDA_POR_QUADRADO)/2) and pos[1] < int((altura+MEDIDA_POR_QUADRADO)/2):
                            pygame.draw.rect(janela, CINZENTO, (int((largura-5*MEDIDA_POR_QUADRADO)/2)+4, int((altura-MEDIDA_POR_QUADRADO)/2)+4, 5*MEDIDA_POR_QUADRADO-8, MEDIDA_POR_QUADRADO-8))
                            label = myfont.render("Restart!", 1, PRETO)
                            janela.blit(label, (int((largura-3*MEDIDA_POR_QUADRADO)/2)+2, int((largura-3*MEDIDA_POR_QUADRADO)/2+MEDIDA_POR_QUADRADO)+2))
                        else:
                            pygame.draw.rect(janela, BRANCO, (int((largura-5*MEDIDA_POR_QUADRADO)/2)+4, int((altura-MEDIDA_POR_QUADRADO)/2)+4, 5*MEDIDA_POR_QUADRADO-8, MEDIDA_POR_QUADRADO-8))
                            label = myfont.render("Restart!", 1, PRETO)
                            janela.blit(label, (int((largura-3*MEDIDA_POR_QUADRADO)/2)+2, int((largura-3*MEDIDA_POR_QUADRADO)/2+MEDIDA_POR_QUADRADO)+2))
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        pos = pygame.mouse.get_pos()
                        if int((largura-5*MEDIDA_POR_QUADRADO)/2) < pos[0] and int((altura-MEDIDA_POR_QUADRADO)/2) < pos[1] and pos[0] < int((largura+5*MEDIDA_POR_QUADRADO)/2) and pos[1] < int((altura+MEDIDA_POR_QUADRADO)/2):
                            game_over = False
                            tabuleiro = criar_tabuleiro()
                            pygame.draw.rect(janela, PRETO, (0, 0, largura, MEDIDA_POR_QUADRADO))
                            time_start = 0

                pygame.display.update()
                #print(time.time())
            desenhar_tabuleiro(tabuleiro, janela, altura)

main()