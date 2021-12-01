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

# Sounds
fire_sound = g.mixer.Sound("assets/shoot.wav")
enemy_kill = g.mixer.Sound("assets/invaderkilled.wav")

# Sprite Groups
all_sprites = g.sprite.Group()
player_group = g.sprite.Group()
missile_group = g.sprite.Group()
enemy_group = g.sprite.Group()

# Player
player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)

# Enemy
for enemin in range (4):
    for val in range(8):
        enemy = Enemy(val, enemin, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)

# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        if event.type == g.KEYDOWN:
            if event.key == g.K_SPACE:
                missile = Missile(player.rect.centerx-2, player.rect.top)
                missile_group.add(missile)
                all_sprites.add(missile)
                fire_sound.play()

    deadshot = g.sprite.groupcollide(missile_group, enemy_group, True, True)
    if deadshot:
        enemy_kill.play()

    screen.fill(SPACE)

    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    all_sprites.update()

    g.display.flip()
    clock.tick(FPS)