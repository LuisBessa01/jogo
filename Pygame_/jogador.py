##### luis, o Fajuto


import pygame

class Jogador:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.posição_inicial_x = x_inicial
        self.posição_inicial_y = y_inicial

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        self.posição_x = x_inicial
        self.posição_y = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)
    
    def apareça(self, tela):
        tela.blit(self.imagem,(self.posição_x, self.posição_y))
    
    def movimento (self, cima, baixo, esquerda, direita,):
        teclas = pygame.key.get_pressed()
        if teclas [direita]:
            if self.posição_x < 800 - self.largura:
                self.posição_x += 5
            else:
                self.posição_x = 800 - self.largura

        teclas = pygame.key.get_pressed()
        if teclas [esquerda]:
            if self.posição_x > 0: 
                self.posição_x -= 5
            else:
                self.posição_x = 0

        teclas = pygame.key.get_pressed()
        if teclas [cima]:
            if self.posição_y >0:
                self.posição_y -= 5
            else:
                self.posição_y =0
                self.posição_y = self.posição_inicial_y
                self.posição_x = self.posição_inicial_x

        teclas = pygame.key.get_pressed()
        if teclas [baixo]:
            if self.posição_y < 500 - self.altura:
                self.posição_y += 5
            else:
                self.posição_y = 500 - self.altura


                