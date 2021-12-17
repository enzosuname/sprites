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
            if self.rect.x <= DISPLAY_WIDTH:
                self.change_x = 4
        elif keys[g.K_LEFT]:
            if self.rect.x >= 0:
                self.change_x = -4
        else:
            self.change_x = 0

class Enemy(g.sprite.Sprite):

    # y_level = 0
    # change_x = 3

    def __init__(self, xval, yval, image):
        g.sprite.Sprite.__init__(self)

        self.xval = xval
        self.yval = yval
        self.image = g.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = self.xval, self.yval

        self.counter = 0

    def update(self, x_velo):
        self.rect.x += x_velo * 2

class Missile(g.sprite.Sprite):
    def __init__(self, x, y, direction):
        g.sprite.Sprite.__init__(self)

        self.y_velo = 6 * direction

        self.image = g.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        g.draw.rect(self.image, BLUE, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.y_velo

        if self.rect.bottom <= 0 or self.rect.top >= DISPLAY_LENGTH:
            self.kill()

class Block(g.sprite.Sprite):
    def __init__(self, display, x, y):
        g.sprite.Sprite.__init__(self)
        self.image = g.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        g.draw.rect(display, BLOCK_COLOR, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])

class Explosion(g.sprite.Sprite):
    def __init__(self, center):
        g.sprite.Sprite.__init__(self)
        self.image = EXPLOSION[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.framerate = 50
        self.kill_center = center
        self.prev_update = g.time.get_ticks()

    def update(self):
        now = g.time.get_ticks()
        if now - self.prev_update > self.framerate:
            self.prev_update = now
            self.frame += 1
        if self.frame == len(EXPLOSION):
            self.kill()
        else:
            self.image = EXPLOSION[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.kill_center

class UFO(g.sprite.Sprite):
    def __init__(self, xval, yval, image, modifier):
        g.sprite.Sprite.__init__(self)

        self.xval = xval
        self.yval = yval
        self.image = g.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = self.xval, self.yval
        self.counter = 0
        self.modifier = modifier

    def update(self):
        self.rect.x += 3 * self.modifier

        if self.rect.left >= DISPLAY_WIDTH or self.rect.right <= 0:
            self.kill()