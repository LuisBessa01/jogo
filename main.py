##### Luis, o Fajuto


import pygame
#CRIANDO A TELA
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pega Doces")
tela.fill((136, 76, 181))



#CONFIGURAÇÃO PARA RODAR
clock = pygame.time.Clock()

rodando = True

#DENTRO DO JOGO E COLOCANDO DENTRO DELE LA ELE 1000x
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False





    #TELA ATUALIZANDO
    pygame.display.update()
    #FPS
    clock.tick(60)