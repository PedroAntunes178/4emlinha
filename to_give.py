#importes
import numpy as np
import pygame
import sys
import math
import time

#variaveis globais


# definição de cores em RGB
AZUL_NEEC = (0, 157, 224)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PECA1 = (225, 0, 0)
PECA2 = (0, 225, 225)
VERDE = (0, 255, 0)
ROXO = (255, 0, 255)
CINZENTO = (150,150,150)

def criar_tabuleiro():
    pass

def imprimir_tabuleiro(tabuleiro):
    pass

def colocar_peca_no_tabuleiro(tabuleiro, col, player, linha):
    pass

def vitoria(tabuleiro, linha, coluna):
    pass


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

def main():

        if game_over:
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
