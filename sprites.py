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
            if self.rect.x < DISPLAY_WIDTH:
                self.change_x = 4
        elif keys[g.K_LEFT]:
            if self.rect.x > 0:
                self.change_x = -4
        else:
            self.change_x = 0

class Enemy(g.sprite.Sprite):

    y_level = 0
    change_x = 3

    def __init__(self, xval, yval, image):
        g.sprite.Sprite.__init__(self)

        self.xval = xval
        self.yval = yval
        self.image = g.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = self.xval, self.yval
        #self.rect.x = DISPLAY_WIDTH * 3/4 - (100 * xval)

        self.counter = 0

    def update(self):
        self.rect.x += Enemy.change_x
        if self.rect.right == DISPLAY_WIDTH-50 or self.rect.left == 50:
            Enemy.y_level += 1
            self.counter+=1
            self.rect.y += self.rect.height + Enemy.y_level * 50
            Enemy.change_x *= -1
        self.rect.y = Enemy.y_level * 50 + self.counter + self.yval

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