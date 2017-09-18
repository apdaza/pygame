import sys, pygame, util
from pygame.locals import *
from heroe import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def game():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Flappy" )
    background_image = util.cargar_imagen('fondo.jpg');
    pygame.mouse.set_visible( False )
    heroe = Heroe()
    
    while True:       
        heroe.update((SCREEN_WIDTH,SCREEN_HEIGHT))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)      
        pygame.display.update()
        pygame.time.delay(10)

      
if __name__ == '__main__':
      game()

