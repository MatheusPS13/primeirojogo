import pygame
import math

pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

class Cobra:
    #screen: pygame.display.Surface
    dd = 10 # intervalo de desenho
    dx = 1
    dy = 1
    vx = 1
    vy = 0
    vxa = 0
    vya = 1
    tamanho = 0
    acrescimo = 20
    raio_corpo = 10
    cor_corpo = (100,100,100)


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
        self.trajeto = [(self.x,self.y)]

    def distancia(self,x,y):
        dir = ((y[0]-x[0])*1.0,(y[1]-x[1])*1.0)
        td = math.sqrt(dir[0]**2+dir[1]**2)
        return td

    def desenhar_linha(self, x, y, desenhar):
        dir = ((y[0] - x[0])*1.0, (y[1] - x[1])*1.0)
        td = math.sqrt(dir[0] ** 2 + dir[1] ** 2)
        desenho_somado = 0
        if td > 0:
            dir = (dir[0]/td,dir[1]/td)
            xa, ya = x[0], x[1]
            while self.distancia((xa,ya), y)>self.dd:
                pygame.draw.circle(self.screen, self.cor_corpo, (xa, ya), self.raio_corpo)
                xa += dir[0]*self.dd
                ya += dir[1]*self.dd
                desenho_somado += self.dd

                if desenho_somado >= desenhar:
                    break

        return desenho_somado

    def desenhar_corpo(self):

        if len(self.trajeto) < 2:
            x = self.x, self.y
        else:
            x = self.trajeto[-2]
        if len(self.trajeto) <1:
            y = self.x, self.y
        else:
            y = self.trajeto[-1]
        self.desenhar_linha(x, y, 0)


    def desenhar_trajeto(self):

        desenhado = 0
        trajeto_imprimir = self.trajeto[::-1]
        for i,p in enumerate(trajeto_imprimir[:-1]):
            po = trajeto_imprimir[i+1]
            desenhado += self.desenhar_linha(p,po,300)
            if desenhado > self.tamanho*self.acrescimo:
                break
            print(p,po)

    def desenhar(self):

        #self.desenhar_corpo()
        self.desenhar_trajeto()

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

    def guarda_curva(self):
        self.trajeto += [(self.x,self.y)]

    def move_cima(self):
        self.guarda_curva()

        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 0
        self.vy = -1

    def move_baixo(self):
        self.guarda_curva()

        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 0
        self.vy = 1

    def move_direita(self):
        self.guarda_curva()

        self.vxa = self.vx
        self.vya = self.vy

        self.vx = 1
        self.vy = 0

    def move_esquerda(self):
        self.guarda_curva()

        self.vxa = self.vx
        self.vya = self.vy

        self.vx = -1
        self.vy = 0

    def detecta_alimento(self,alimentos):
        for i,a in enumerate(alimentos):
            d = (self.x-a.x)**2+(self.y-a.y)**2
            d = math.sqrt(d)
            if d<15:
                del(alimentos[i])
                self.tamanho += 1
