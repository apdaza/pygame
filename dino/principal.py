import sys, pygame, util
from pygame.locals import *
from heroe import *
from obstaculo import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def game():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Dino running" )
    background_image = util.cargar_imagen('png/BG/BG.png');
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.mouse.set_visible( False )
    heroe = Heroe()
    obstaculo = Obstaculo((SCREEN_WIDTH-64,SCREEN_HEIGHT-64))

    while True:
        heroe.update((SCREEN_WIDTH,SCREEN_HEIGHT))
        obstaculo.update((SCREEN_WIDTH,SCREEN_HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            heroe.reinit()
            obstaculo.reinit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(obstaculo.image, obstaculo.rect)
        if heroe.rect.colliderect(obstaculo.rect):
            heroe.estado = 0
            obstaculo.estado = 0
            obstaculo.explosion()
        pygame.display.update()
        pygame.time.delay(10)


if __name__ == '__main__':
      game()
