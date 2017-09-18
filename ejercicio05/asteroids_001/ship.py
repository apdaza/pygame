import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *

class Ship(Sprite):
    def __init__(self, contenedor):
        Sprite.__init__(self)
        self.puntos = 0
        self.vida = 100
        self.vel = [0,0]
        self.contenedor = contenedor
        self.image = pygame.image.load("imagenes/ship.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(contenedor[0]/2, contenedor[1]/2)
        
    def update(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_LEFT]:
            pass
        elif teclas[K_RIGHT]:
            pass
        elif teclas[K_UP]:
            pass
        elif teclas[K_DOWN]:
            pass
          
