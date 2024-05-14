#####Luis, o Fajuto


import random
import pygame
from jogador import *
from obstaculos import *
pygame.init()

#CONFIGURAÇÃO DA TELA
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("As Ruas Mortíferas")
tela.fill((136, 76, 181))
fundo = pygame.image.load("imagens/estrada.png")
fundo = pygame.transform.scale(fundo, (800,500))
#CARREGANDO IMAGENS
pontos_j1 = 0
pontos_j2 = 0
jogador1 = Jogador("imagens/hamster.png", 45, 50, 355, 450)
jogador2 = Jogador("imagens/vaca.png", 150, 80, 325, 420)
lista_carros = [Carros("imagens/carro-1.png",80, 50, 800, 50, random.randint(-7, -3)),
                Carros("imagens/carro-2.png",80, 50, 800, 400, random.randint(-7, -3)),
                Carros("imagens/carro-3.png",80, 50, 800, 200, random.randint(-7, -3)),
                Carros("imagens/carro-1.png",80, 50, 800, 300, random.randint(-7, -3))]


fonte = pygame.font.SysFont("Comic Sans", 20, True)
#CONFIG FPS
clock = pygame.time.Clock()

rodando = True
while rodando:
    #TRATANDO EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((136, 76, 181))
    #DESENHANDO OS OBJETOS
    tela.blit(fundo,(0,0))

    for carro_lista in lista_carros:
        carro_lista.apareça(tela)
        carro_lista.corrida()

        if jogador1.mascara.overlap(carro_lista.mascara, (carro_lista.posição_x - jogador1.posição_x , carro_lista.posição_y - jogador1.posição_y)):
            jogador1.posição_x = 355
            jogador1.posição_y = 450
        if jogador2.mascara.overlap(carro_lista.mascara, (carro_lista.posição_x - jogador2.posição_x , carro_lista.posição_y - jogador2.posição_y)):
            jogador2.posição_x = 325
            jogador2.posição_y = 420

    texto_ponto_vaca = fonte.render(f"PONTOS VACA:", True, (0,255,0))
    texto_ponto_hamster = fonte.render(f"PONTOS HAMSTER:{pontos_j1}", True, (0,255,0))
    tela.blit(texto_ponto_vaca,(0,5))
    tela.blit(texto_ponto_hamster,(0,24))
    

    jogador1.movimento(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareça(tela)

    jogador2.movimento(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    jogador2.apareça(tela)
    #COLISÕES



    pygame.display.update()

    #CONFIGURANDO FPS
    clock.tick(60)