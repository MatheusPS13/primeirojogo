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
        self.corpo = []

    def distancia(self,x,y):
        dir = ((y[0]-x[0])*1.0,(y[1]-x[1])*1.0)
        td = math.sqrt(dir[0]**2+dir[1]**2)
        return td

    def desenhar_linha(self, x, y, desenhado):
        dir = ((y[0] - x[0])*1.0, (y[1] - x[1])*1.0)
        td = math.sqrt(dir[0] ** 2 + dir[1] ** 2)
        desenho_somado = 0
        if desenhado >= self.tamanho:
            return desenhado
        if td > 0:
            dir = (dir[0]/td,dir[1]/td)
            xa, ya = x[0], x[1]
            while self.distancia((xa,ya), y)>self.dd:
                if desenho_somado+desenhado >= self.tamanho:
                    break
                self.corpo += [(xa+1.4*self.raio_corpo, ya+1.4*self.raio_corpo)]
                #pygame.draw.circle(self.screen, self.cor_corpo, (xa+1.4*self.raio_corpo, ya+1.4*self.raio_corpo), self.raio_corpo)
                xa += dir[0]*self.dd
                ya += dir[1]*self.dd
                desenho_somado += self.dd

        return desenho_somado+desenhado

    def desenhar_corpo(self):

        for p in self.corpo:
            pygame.draw.circle(self.screen, self.cor_corpo, p, self.raio_corpo)

    def pescoco(self,desenhado):
        return self.desenhar_linha((self.x,self.y),self.trajeto[-1],desenhado)

    def desenhar_trajeto(self,desenhado):

        desenhado_a = desenhado
        trajeto_imprimir = self.trajeto[::-1]
        for i,p in enumerate(trajeto_imprimir[:-1]):
            po = trajeto_imprimir[i+1]
            desenhado_a += self.desenhar_linha(p,po,desenhado_a)
            if desenhado_a > self.tamanho:
                break
        return desenhado_a

    def testa_colide(self):
        for c in self.corpo:
            td = self.distancia((self.x,self.y),c)
            if td < self.raio_corpo*0.4:
                print('Game over!')


    def desenhar(self):

        self.corpo = []
        des = self.pescoco(0)
        des = self.desenhar_trajeto(des)
        self.desenhar_corpo()

        self.testa_colide()


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
                self.tamanho += self.acrescimo
