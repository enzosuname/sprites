import pygame as g
import math as m
import random as r
from settings import *

class Player(g.sprite.Sprite):
    def __init__(self, image_path):
        g.sprite.Sprite.__init__(self)

        self.image = g.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = DISPLAY_WIDTH // 2
        self.rect.y = DISPLAY_LENGTH - self.rect.height

        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x

        keys = g.key.get_pressed()
        if keys[g.K_RIGHT]:
                self.change_x = 4
        elif keys[g.K_LEFT]:
                self.change_x = -4

class Enemy():
    pass

class Missile():
    pass