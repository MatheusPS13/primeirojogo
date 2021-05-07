import pygame
import cobra, alimento

pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

(width,height) = (600,600)
size_screen = (width,height)

vel_jogo = 20

def cria_alimentos(screen, n):
    alims = [alimento.Alimento(screen) for i in range(n)]

    return alims

def desenha_alimentos(alims):
    for a in alims:
        a.desenhar()

def main():
    pygame.init()

    logo = pygame.image.load(pasta_imagens+"cabeca.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Jogo da Cobrinha")

    screen = pygame.display.set_mode(size_screen)
    alims = cria_alimentos(screen, 5)

    #clock = pygame.time.clock()
    fundo = pygame.image.load(pasta_imagens+"fundo.png")
    screen.blit(fundo,[0,0])

    c = cobra.Cobra(screen)
    desenha_alimentos(alims)
    c.desenhar()

    a = alimento.Alimento(screen)


    running = True

    while running:
        # event handling, gets all event from the event queue
        pygame.display.update()

        c.andar()

        screen.blit(fundo, [0, 0])
        desenha_alimentos(alims)

        c.desenhar()
        #c.desenhar_linha((50,50), (250,50), 0)

        c.detecta_alimento(alims)

        pygame.time.wait(vel_jogo)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    c.move_esquerda()
                elif event.key == pygame.K_RIGHT:
                    c.move_direita()
                elif event.key == pygame.K_UP:
                    c.move_cima()
                elif event.key == pygame.K_DOWN:
                    c.move_baixo()


            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
