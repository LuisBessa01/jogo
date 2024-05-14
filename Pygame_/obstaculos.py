##### Luis, o Fajuto


import pygame
import random

class Carros:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial,carro_velocidade):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.velocidade = carro_velocidade

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        self.posição_x = x_inicial
        self.posição_y = y_inicial
        
        self.mascara = pygame.mask.from_surface(self.imagem)
    
    def apareça(self, tela):
        tela.blit(self.imagem,(self.posição_x, self.posição_y))
    
    def corrida(self):
        if self.posição_x > -100:
            self.posição_x += self.velocidade
        else:
            self.posição_x = 900
            self.velocidade = random.randint(-7, -3)

