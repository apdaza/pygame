import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Obstaculo(Sprite):
    def __init__(self, pos):
        Sprite.__init__(self)
        self.cont = 0
        self.image = util.cargar_imagen('png/Object/Stone.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
        self.vel = -1
        self.estado = 1

    def update(self,size):
        if self.estado == 1:
            self.rect.x = (self.rect.x + self.vel) % size[0]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect.size = (64,64)

    def explosion(self):
        self.image = util.cargar_imagen('png/Object/explosion.png')

    def reinit(self):
        self.image = util.cargar_imagen('png/Object/Stone.png')
        self.estado = 1
