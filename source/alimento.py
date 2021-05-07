import pygame, random

pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]


class Alimento:

    def __init__(self, screen):
        self.imagem = pygame.image.load(pasta_imagens + 'alimento.png')

        self.screen = screen
        self.wwidth = screen.get_width()
        self.wheight = screen.get_height()
        self.x = random.randint(10,self.wwidth-10)
        self.y = random.randint(10,self.wheight-10)


    def desenhar(self):
        self.screen.blit(self.imagem, [self.x, self.y])
