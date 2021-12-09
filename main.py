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
offset = 175

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
for row in range (2):
    for col in range(10):
        enemy = Enemy(offset+50*col, 310 + 50 * row, RED_ALIEN)
        enemy_group.add(enemy)
for row in range (2):
    for col in range(10):
        enemy = Enemy(offset+50*col, 210 + 50 * row, YELLOW_ALIEN)
        enemy_group.add(enemy)
for row in range (2):
    for col in range(10):
        enemy = Enemy(offset+50*col, 110 + 50 * row, GREEN_ALIEN)
        enemy_group.add(enemy)

clock = g.time.Clock()
missile_previous_fire = g.time.get_ticks()

# game
running = True
enemy_direction = 1

while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        if event.type == g.KEYDOWN:
            if event.key == g.K_SPACE:
                missile_current_fire = g.time.get_ticks()
                if missile_current_fire - missile_previous_fire >= MISSILE_DELAY:
                    missile_previous_fire = missile_current_fire
                    missilePLAYER = Missile(player.rect.centerx-2, player.rect.top, 1)
                    missile_groupPLAYER.add(missilePLAYER)
                    all_sprites.add(missilePLAYER)
                    fire_sound.play()

    if len(missile_groupENEMY) <= len(enemy_group)/5:
        missileENEMY = Missile(r.randint(100, DISPLAY_WIDTH-100), enemy.rect.top, -1)
        missile_groupENEMY.add(missileENEMY)
        all_sprites.add(missileENEMY)
        if lives <= 0 or len(enemy_group) == 0:
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

    enemies = enemy_group.sprites()
    for enemy in enemies:
        if enemy.rect.right >= DISPLAY_WIDTH - 50:
            enemy_direction = -1

            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

        elif enemy.rect.left <= 50:
            enemy_direction = 1

            if enemies:
                for alien in enemies:
                    alien.rect.y += 4

    screen.fill(SPACE)

    enemy_group.draw(screen)
    missile_groupPLAYER.draw(screen)
    missile_groupENEMY.draw(screen)
    player_group.draw(screen)

    enemy_group.update(enemy_direction)
    all_sprites.update()
    # missile_groupPLAYER.update()
    # missile_groupENEMY.update()
    # player_group.update()


    g.display.flip()
    clock.tick(FPS)