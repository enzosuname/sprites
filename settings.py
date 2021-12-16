import math as m
import pygame as g

# Create color constants

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SPACE = (29, 17, 53)
WHITE = (255, 255, 255)
BLOCK_COLOR = (252, 53, 3)
GREEN = (0, 255, 0)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 800
DISPLAY_LENGTH = 990
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60

# missile
MISSILE_WIDTH = 5
MISSILE_HEIGHT = 15
MISSILE_DELAY = 300
BOMB_DELAY = 300

# Images
PLAYER = "assets/player.png"
RED_ALIEN = "assets/red.png"
GREEN_ALIEN = "assets/green.png"
YELLOW_ALIEN = "assets/yellow.png"

# Font

g.font.init()
END = g.font.Font('assets/unifont.ttf', 80)
SCORE = g.font.Font('assets/unifont.ttf', 60)
START = g.font.Font('assets/unifont.ttf', 30)

# Explosion
EXPLOSION = []
for i in range (0,8):
    EXPLOSION.append(g.transform.scale(g.image.load(f'assets/sprite_{i}.png'), (50, 50)))

# Block
BLOCK_WIDTH = 7
BLOCK_HEIGHT = 7

LAYOUT = ["00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000100000000000000000000000000000010000000000",
          "00000001110000000000000000000000000000111000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000"]

SHEILD = [
    "  xxxxxxx",
    " xxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxx     xxx",
    "xx       xx"
]

print(len(LAYOUT[0]))
