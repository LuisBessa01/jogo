##### Luis, o Fajuto


import pygame

class Jogadorjogo:

    def __init__ (self, arquivo_imagem, largura_imagem, altura_imagem, posição_inicial_x, posição_inicial_y):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.x_inicial = posição_inicial_x
        self.y_inicial = posição_inicial_y


        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

    def apareça (self, tela):
        tela.blit(self.imagem, (self.x_inicial, self.y_inicial))