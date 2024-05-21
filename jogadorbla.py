##### Luis, o Fajuto


import pygame

class Jogadorjogo:

    def __init__ (self, arquivo_imagem, largura_imagem, altura_imagem, posição_inicial_x, posição_inicial_y):
        #CARACTERISTICAS FIXAS
        self.imagem = pygame.image.load(arquivo_imagem)
        self.largura = largura_imagem
        self.altura = altura_imagem
        self.x_inicial = posição_inicial_x
        self.y_inicial = posição_inicial_y
        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

        #CARACTERISTICAS MUTAVEIS
        self.posição_x = posição_inicial_x
        self.posição_y = posição_inicial_y

        #MASCARA
        self.mascara = pygame.mask.from_surface(self.imagem)
        #PODER!!!
        self.limite = 0


    def apareça (self, tela):
        tela.blit(self.imagem, (self.posição_x, self.posição_y))

    def movimento (self, esquerda, direita):
        tecla_apertada = pygame.key.get_pressed()
        
        if tecla_apertada [esquerda]:
            if self.posição_x > 0: 
                self.posição_x -= 10
            else:
                self.posição_x = 0
        if tecla_apertada [direita]:
            if self.posição_x < 800:
                self.posição_x += 10
            else:
                self.posição_x = 800 - self.largura
            