import pygame

pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

class Cobra:
    #screen: pygame.display.Surface
    dx = 1
    dy = 1
    vx = 1
    vy = 0
    vxa = 0
    vya = 1


    def __init__(self, screen):
        self.cabeca_d = pygame.image.load(pasta_imagens + 'cabeca_d.png')
        self.cabeca_e = pygame.image.load(pasta_imagens + 'cabeca_e.png')
        self.cabeca_c = pygame.image.load(pasta_imagens + 'cabeca_c.png')
        self.cabeca_b = pygame.image.load(pasta_imagens + 'cabeca_b.png')
        self.cabeca_df = pygame.image.load(pasta_imagens + 'cabeca_df.png')
        self.cabeca_ef = pygame.image.load(pasta_imagens + 'cabeca_ef.png')
        self.cabeca_cf = pygame.image.load(pasta_imagens + 'cabeca_cf.png')
        self.cabeca_bf = pygame.image.load(pasta_imagens + 'cabeca_bf.png')
        self.screen = screen
        self.x = 300
        self.y = 300
        self.wwidth = screen.get_width()
        self.wheight = screen.get_height()

    def desenhar(self):
        if self.vx>0:
            if self.vxa <0 :
                self.screen.blit(self.cabeca_df, [self.x, self.y])
            else:
                self.screen.blit(self.cabeca_d, [self.x, self.y])
        elif self.vx <0:
            if self.vxa>0:
                self.screen.blit(self.cabeca_ef, [self.x, self.y])
            else:
                self.screen.blit(self.cabeca_e, [self.x, self.y])
        elif self.vy>0:
            if self.vya <0:
                self.screen.blit(self.cabeca_bf, [self.x, self.y])
            else:
                self.screen.blit(self.cabeca_b, [self.x, self.y])
        elif self.vy<0:
            if self.vya >0:
                self.screen.blit(self.cabeca_cf, [self.x, self.y])
            else:
                self.screen.blit(self.cabeca_c, [self.x, self.y])

    def andar(self):
        self.x += self.dx*self.vx
        self.y += self.dy*self.vy
        if self.x > self.wwidth:
            self.x -= self.wwidth
        if self.y > self.wheight:
            self.y -= self.wheight
        if self.x <0:
            self.x += self.wwidth
        if self.y <0:
            self.y += self.wheight


    def move_cima(self):
        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 0
        self.vy = -1

    def move_baixo(self):
        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 0
        self.vy = 1

    def move_direita(self):
        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 1
        self.vy = 0

    def move_esquerda(self):
        self.vxa = self.vx
        self.vya = self.vy

        self.vx = -1
        self.vy = 0
