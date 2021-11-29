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
            if self.rect.x <=DISPLAY_WIDTH:
                self.change_x = 4
        elif keys[g.K_LEFT]:
            if self.rect.x >= 0:
                self.change_x = -4

class Enemy(g.sprite.Sprite):
    def __init__(self, xval, yval, image):
        g.sprite.Sprite.__init__(self)

        self.xval = xval
        self.yval = yval
        self.image = g.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH - (100 * xval), self.rect.height - (50*yval)

        self.y_velo = 0
        self.x_velo = 2

    def update(self):
        self.rect.y += self.y_velo
        self.rect.x += self.x_velo
        if self.rect.x == DISPLAY_WIDTH-50:
            self.x_velo = -2
            self.rect.y += self.rect.height
        if self.rect.x == 50:
            self.x_velo = 2
            self.rect.y += self.rect.height

class Missile(g.sprite.Sprite):
    def __init__(self, x, y):
        g.sprite.Sprite.__init__(self)

        self.y_velo = 6

        self.image = g.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        g.draw.rect(self.image, BLUE, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.y_velo

        if self.rect.bottom <= 0:
            self.kill()