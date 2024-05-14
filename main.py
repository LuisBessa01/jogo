##### Luis, o Fajuto


import pygame
from jogadorbla import *
from objetos import *
import random
#CRIANDO A TELA
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pega Doces")
tela.fill((136, 76, 181))
fundo = pygame.image.load("zimagens/fundo.png")
fundo = pygame.transform.scale(fundo,(800,500))


#JOGADOR ATRIBUTOS E TAL
jogador = Jogadorjogo("zimagens/copo.png", 45, 50, 355, 420)

#LISTA DOS OBJETOS JOGADOS

#CONFIGURAÇÃO PARA RODAR
clock = pygame.time.Clock()

rodando = True

#DENTRO DO JOGO E COLOCANDO DENTRO DELE LA ELE 1000x
while rodando == True:
    #CLICKAR PARA FECHAR
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    #LIMPANDO A TELA
    tela.fill((136, 76, 181))
    tela.blit(fundo, (0,0))

    #JOGADOR APARECENDO e ANDANDO
    jogador.movimento(pygame.K_LEFT, pygame.K_RIGHT)
    jogador.apareça(tela)   






    #TELA ATUALIZANDO
    pygame.display.update()
    #FPS
    clock.tick(60)