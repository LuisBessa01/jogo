##### Luis, o Fajuto


import pygame
#CRIANDO A TELA
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pega Doces")


rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False