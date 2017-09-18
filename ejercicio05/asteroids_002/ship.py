import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *

class Ship(Sprite):
    def __init__(self, contenedor):
        Sprite.__init__(self)
        self.angulo = 0
        self.puntos = 0
        self.vida = 100
        self.vel = [0,0]
        self.contenedor = contenedor
        self.base_image = pygame.image.load("imagenes/ship.png")
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.move_ip(contenedor[0]/2, contenedor[1]/2)
        
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.rotar(2)
        elif teclas[K_RIGHT]:
            self.rotar(-2)
        elif teclas[K_UP]:
            self.acelerar()
        elif teclas[K_DOWN]:
            pass
          
        self.vel[0] *= 0.99
        self.vel[1] *= 0.99
        self.rect = self.rect.move(self.vel)
        self.rect.x = self.rect.x % self.contenedor[0]
        self.rect.y = self.rect.y % self.contenedor[1]
    
    def acelerar(self):
        self.vel[0] += math.cos(math.radians((self.angulo)%360))
        self.vel[1] -= math.sin(math.radians((self.angulo)%360))

    def rotar(self, angulo):
        self.angulo += angulo
        centerx = self.rect.centerx
        centery = self.rect.centery
        self.image = pygame.transform.rotate(self.base_image, self.angulo)
        self.rect = self.image.get_rect() 
        self.rect.centerx = centerx
        self.rect.centery = centery
