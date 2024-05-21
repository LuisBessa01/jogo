##### Luis, o Fajuto


import pygame
from jogadorbla import *
from objetos import *
import random

pygame.init()

#CRIANDO A TELA
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pega Doces")
tela.fill((136, 76, 181))
fundo = pygame.image.load("zimagens/fundo.png")
fundo = pygame.transform.scale(fundo,(800,500))
pontos = 0

fonte = pygame.font.SysFont("Arial", 20, True)

#JOGADOR ATRIBUTOS E TAL
jogador = Jogadorjogo("zimagens/copo.png", 45, 50, 355, 420)

#LISTA DOS OBJETOS JOGADOS



lista_objetos = [Doce("zimagens/doce1.png", 45, 50),
                 Doce("zimagens/doce1.png", 45, 50),
                 Doce("zimagens/doce1.png", 45, 50),
                 Doce("zimagens/doce1.png", 45, 50),
                 Vegetais("zimagens/brocolis.png", 45, 50),
                 Vegetais("zimagens/brocolis.png", 45, 50),
                 Vegetais("zimagens/brocolis.png", 45, 50),
]

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

        if jogador.mascara.overlap(objeto.mascara, (objeto.posição_x - jogador.posição_x , objeto.posição_y - jogador.posição_y)):
            if objeto.gostoso == True:
                pontos += random.randint(5,15)
            else:
                pontos -= 10
            objeto.posição_y = 0-objeto.altura
            objeto.posição_x = random.randint(0,800-objeto.largura)
    texto_ponto = fonte.render(f"PONTOS:{pontos}", True, (0,255,0))
    tela.blit(texto_ponto, (0,5))

    #TELA ATUALIZANDO
    pygame.display.update()
    #FPS
    clock.tick(60)