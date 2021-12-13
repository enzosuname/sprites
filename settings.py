import math as m

# Create color constants

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPACE = (29, 17, 53)
WHITE = (255, 255, 255)
BLOCK_COLOR = (252, 53, 3)

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
