##### Luis, o Fajuto


import pygame
import random
class Doce:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem,):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.velocidade = random.randint(2, 5)

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        self.posição_x = random.randint(0,800-self.largura)
        self.posição_y = 0-self.altura

    def apareça (self, tela):
        tela.blit(self.imagem, (self.posição_x, self.posição_y))

    def movimento(self):
        if self.posição_y < 500:
            self.posição_y += self.velocidade
        else:
            self.posição_y = 0-self.altura
            self.posição_x = random.randint(0,800-self.largura)
            self.velocidade = random.randint(2, 5)

class Vegetais:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem,):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.velocidade = random.randint(3, 8)

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        self.posição_x = random.randint(0,800-self.largura)
        self.posição_y = 0-self.altura

    def apareça (self, tela):
        tela.blit(self.imagem, (self.posição_x, self.posição_y))

    def movimento(self):
        if self.posição_y < 500:
            self.posição_y += self.velocidade
        else:
            self.posição_y = 0-self.altura
            self.posição_x = random.randint(0,800-self.largura)
            self.velocidade = random.randint(3, 8)