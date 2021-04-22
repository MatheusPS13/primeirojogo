import pygame
import cobra

pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

(width,height) = (600,600)
size_screen = (width,height)

def main():
    pygame.init()

    logo = pygame.image.load(pasta_imagens+"cabeca.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Jogo da Cobrinha")

    screen = pygame.display.set_mode(size_screen)


    #clock = pygame.time.clock()
    fundo = pygame.image.load(pasta_imagens+"fundo.png")
    screen.blit(fundo,[0,0])

    cabeca = pygame.image.load(pasta_imagens+'cabeca.png')
    c = cobra.Cobra(screen)
    c.desenhar()

    running = True

    while running:
        # event handling, gets all event from the event queue
        pygame.display.update()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()