import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('png/Run (1).png'),
                                        util.cargar_imagen('png/Run (2).png'),
                                        util.cargar_imagen('png/Run (3).png'),
                                        util.cargar_imagen('png/Run (4).png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 200)
        self.vel = [2,6]
        self.estado = 1

    def reinit(self):
        self.rect.x += 50
        self.estado = 1

    def update(self,size):
        if self.estado == 1:
            teclas = pygame.key.get_pressed()
            if teclas[K_UP] and self.rect.y>=10:
                self.rect.y -= 10
            if teclas[K_RIGHT] and self.vel[0] < 5:
                self.vel[0] += 1
            if teclas[K_LEFT] and self.vel[0] > 1:
                self.vel[0] -= 1
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]
            if self.rect.y < size[1] - 128:
                self.rect.y += self.vel[1]
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.cont]
        else:
            self.image = util.cargar_imagen('png/Dead (5).png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect.size = (68,100)
