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

bala1 = Doce("zimagens/doce1.png", 45, 50)
bala2 = Doce("zimagens/doce1.png", 45, 50)
bala3 = Doce("zimagens/doce1.png", 45, 50)
bala4 = Doce("zimagens/doce1.png", 45, 50)
bala5 = Doce("zimagens/doce1.png", 45, 50)
vegetal1 = Vegetais("zimagens/brocolis.png", 45, 50)
vegetal2 = Vegetais("zimagens/brocolis.png", 45, 50)
vegetal3 = Vegetais("zimagens/brocolis.png", 45, 50)

lista_objetos = [bala1,bala2,bala3,bala4,bala5,vegetal1,vegetal2,vegetal3]

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

    for objeto in lista_objetos:
        objeto.apareça(tela)
        objeto.movimento()


    #TELA ATUALIZANDO
    pygame.display.update()
    #FPS
    clock.tick(60)