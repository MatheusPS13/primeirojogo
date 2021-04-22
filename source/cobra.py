import pygame


class Cobra:
    screen: pygame.display.Surface
    dx = 5
    dy = 5

    def __init__(self, screen):
        self.cabeca = pygame.image.load(pasta_imagens + 'cabeca.png')
        self.screen = screen
        self.x = 300
        self.y = 300

    def desenhar(self):
        self.screen.blit(self.cabeca, [self.x, self.y])

    def move_cima(self):
        self.y += dy

    def move_baixo(self):
        self.y -= dy

    def move_direita(self):
        self.x += dx

    def move_esquerda(self):
        self.x -= dx
