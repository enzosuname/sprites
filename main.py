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
lives = 3

# Sounds
fire_sound = g.mixer.Sound("assets/shoot.wav")
enemy_kill = g.mixer.Sound("assets/invaderkilled.wav")

# Sprite Groups
all_sprites = g.sprite.Group()
player_group = g.sprite.Group()
missile_groupPLAYER = g.sprite.Group()
missile_groupENEMY = g.sprite.Group()
enemy_group = g.sprite.Group()

# Player
player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)

# Enemy
for enemin in range (2):
    for val in range(8):
        enemy = Enemy(100+50*val, 210 + 50*enemin, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
for enemin in range (2):
    for val in range(8):
        enemy = Enemy(100+50*val, 110 + 50*enemin, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
for enemin in range (2):
    for val in range(8):
        enemy = Enemy(100+50*val, 10 + 50*enemin, GREEN_ALIEN)
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
                missilePLAYER = Missile(player.rect.centerx-2, player.rect.top, 1)
                missile_groupPLAYER.add(missilePLAYER)
                all_sprites.add(missilePLAYER)
                fire_sound.play()

    if len(missile_groupENEMY) <= len(enemy_group)/4:
        missileENEMY = Missile(r.randint(10, DISPLAY_WIDTH-10), enemy.rect.bottom, -1)
        missile_groupENEMY.add(missileENEMY)
        all_sprites.add(missileENEMY)
        if lives <= 0:
            missileENEMY.kill()

    deadshot = g.sprite.groupcollide(missile_groupPLAYER, enemy_group, True, True)
    playershot = g.sprite.groupcollide(missile_groupENEMY, player_group, True, False)
    if deadshot:
        enemy_kill.play()
    if playershot:
        lives -= 1
        print(lives)
        if lives <= 0:
            player.kill()
            enemy_group.empty()

    screen.fill(SPACE)

    enemy_group.draw(screen)
    missile_groupPLAYER.draw(screen)
    missile_groupENEMY.draw(screen)
    player_group.draw(screen)
    all_sprites.update()


    g.display.flip()
    clock.tick(FPS)