import pygame as g # in terminal -> pip install pygame
import math as m
from settings import *
from sprites import Player, Enemy, Missile, Block, Explosion
import random as r

#########################################################

g.init()

def gameover():
    screen = g.display.set_mode(SIZE)
    clock = g.time.Clock()

    running = True
    while running:
        for event in g.event.get():
            if event.type == g.QUIT:
                quit()
            if event.type == g.KEYDOWN:
                if event.key == g.K_r:
                    running = False

        screen.fill(SPACE)

        if result == False:
            text = END.render(f"YOU WIN", True, GREEN)
            screen.blit(text, [240, 400])
        if result == True:
            text = END.render(f"GAME OVER", True, RED)
            screen.blit(text, [210, 400])

        text = SCORE.render(f"High Score : {score}", True, WHITE)
        screen.blit(text, [175, 500])
        text = SCORE.render(f"If you wish to reset,", True, WHITE)
        screen.blit(text, [85, 600])
        text = SCORE.render(f"press the 'r' key", True, WHITE)
        screen.blit(text, [125, 650])

        g.display.flip()
        clock.tick(FPS)

def start():
    screen = g.display.set_mode(SIZE)
    clock = g.time.Clock()

    running = True
    while running:
        for event in g.event.get():
            if event.type == g.QUIT:
                quit()
            if event.type == g.KEYDOWN:
                if event.key == g.K_SPACE:
                    return True

        screen.fill(SPACE)

        text = SCORE.render(f"Welcome to Space Invaders", True, WHITE)
        screen.blit(text, [17.5, 100])
        text = START.render(f"Hit your enemies while dodging missiles", True, WHITE)
        screen.blit(text, [100, 250])
        text = START.render(f"Regular Aliens get one point, and UFOs grant 5", True, WHITE)
        screen.blit(text, [50, 400])
        text = START.render(f"Stick behind cover,", True, WHITE)
        screen.blit(text, [275, 550])
        text = START.render(f"and be sure not to be hit three times!", True, WHITE)
        screen.blit(text, [125, 600])
        text = SCORE.render(f"PRESS SPACE TO BEGIN", True, WHITE)
        screen.blit(text, [100, 700])

        g.display.flip()
        clock.tick(FPS)

def play():

    # game dependents

    screen = g.display.set_mode(SIZE)
    g.display.set_caption("Jame Scene")
    clock = g.time.Clock()
    lives = 3
    offset = 175
    global result
    result = ""

    # Sounds
    fire_sound = g.mixer.Sound("assets/shoot.wav")
    enemy_kill = g.mixer.Sound("assets/invaderkilled.wav")

    # Sprite Groups
    all_sprites = g.sprite.Group()
    player_group = g.sprite.Group()
    missile_groupPLAYER = g.sprite.Group()
    missile_groupENEMY = g.sprite.Group()
    block_group = g.sprite.Group()
    explosion_group = g.sprite.Group()
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

    # create shields
    start_values = [50, 262.5, 462.5, 675]
    for start in start_values:
        for row_index, row in enumerate(SHEILD):
            #print(row_index, row)
            for col_index, col in enumerate(row):
                if col == 'x':
                    x_pos = col_index * BLOCK_WIDTH + start
                    y_pos = row_index * BLOCK_HEIGHT + 800
                    block = Block(screen, x_pos, y_pos)
                    block_group.add(block)

    # timing

    clock = g.time.Clock()
    missile_previous_fire = g.time.get_ticks()
    bomb_previous_fire = g.time.get_ticks()

    # game
    running = True
    enemy_direction = 1
    global score
    score = 0

    while running:
        for event in g.event.get():
            if event.type == g.QUIT:
                quit()
            if event.type == g.KEYDOWN:
                if event.key == g.K_SPACE:
                    if lives > 0:
                        missile_current_fire = g.time.get_ticks()
                        if missile_current_fire - missile_previous_fire >= MISSILE_DELAY:
                            missile_previous_fire = missile_current_fire
                            missilePLAYER = Missile(player.rect.centerx-2, player.rect.top, 1)
                            missile_groupPLAYER.add(missilePLAYER)
                            all_sprites.add(missilePLAYER)
                            fire_sound.play()
                elif event.key == g.K_ESCAPE:
                    lives = 0
                elif event.key == g.K_BACKSPACE:
                    enemy_group.empty()

        deadshot = g.sprite.groupcollide(missile_groupPLAYER, enemy_group, True, True)
        playershot = g.sprite.groupcollide(missile_groupENEMY, player_group, True, False)
        barrier = g.sprite.groupcollide(all_sprites, block_group, True, True)
        barrierenemy = g.sprite.groupcollide(enemy_group, block_group, False, True)

        if deadshot:
            enemy_kill.play()
            score += 1
            for hit in deadshot:
                explosion = Explosion(hit.rect.center)
                explosion_group.add(explosion)
                all_sprites.add(explosion)

        if playershot:
            lives -= 1
            print(lives)
            explosion = Explosion(player.rect.center)

            explosion_group.add(explosion)
            all_sprites.add(explosion)

        enemies = enemy_group.sprites()
        for enemy in enemies:
            if enemy.rect.right >= DISPLAY_WIDTH - 50:
                enemy_direction = -1

                if enemies:
                    for alien in enemies:
                        alien.rect.y += 2
                        if alien.rect.y >= 950:
                            lives = 0

            elif enemy.rect.left <= 50:
                enemy_direction = 1

                if enemies:
                    for alien in enemies:
                        alien.rect.y += 4

        if len(missile_groupENEMY) <= len(enemy_group) / 5:
            bomb_current_fire = g.time.get_ticks()
            if bomb_current_fire - bomb_previous_fire >= BOMB_DELAY:
                bomb_previous_fire = bomb_current_fire
                missileENEMY = Missile(r.choice(enemies).rect.top, enemy.rect.top, -1)
                missile_groupENEMY.add(missileENEMY)
                all_sprites.add(missileENEMY)
                if lives <= 0 or len(enemy_group) == 0:
                    missileENEMY.kill()

        screen.fill(SPACE)

        enemy_group.draw(screen)
        block_group.draw(screen)
        all_sprites.draw(screen)

        enemy_group.update(enemy_direction)
        block_group.update()
        all_sprites.update()

        scoretext = SCORE.render(f"SCORE : {score}", True, WHITE)
        screen.blit(scoretext, [25, 10])

        for life in range(lives):
            screen.blit(g.image.load(PLAYER), [700 - 100 * life, 25])

        if lives <= 0:
            all_sprites.empty()
            enemy_group.empty()
            result = True
            return True
        elif len(enemy_group) == 0:
            result = False
            return False

        g.display.flip()
        clock.tick(FPS)

start()

while True:
    play()
    gameover()
