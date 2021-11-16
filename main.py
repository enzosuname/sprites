import pygame as g # in terminal -> pip install pygame
import math as m
from settings import *
from sprites import Player, Enemy, Missile
import random as r

#########################################################

g.init()

# game dependents

screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()

player_group = g.sprite.Group()
player = Player("assets/sprite_ship_3.png")
player_group.add(player)

# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    screen.fill(SPACE)

    player_group.draw(screen)
    player_group.update()

    g.display.flip()
    clock.tick(FPS)