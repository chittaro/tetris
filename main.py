import pygame as py
from pygame.locals import *
from objects.Matrix import Matrix
from objects.Tetromino import Tetromino
from objects.Text import *
from constants import *
import time

GREY = (200, 200, 200)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize game & clock
py.init()
py.font.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Tetris")
clock = py.time.Clock()

# Initialize & blit background
background = py.Surface(screen.get_size()).convert()
background.fill(GREY)
screen.blit(background, (0, 0))
py.display.flip()

# Initialize Matrix (grid)
matrix = Matrix()

# Initialize Tetromino
tetromino = Tetromino(screen, matrix.grid, background)

score = 0
text_with_bg(text=str(score), text_color=BLACK, size=80, 
                pos=(50, 50), bg_color=GREY, screen=screen)
running = True
while running:
    clock.tick(60)

    for event in py.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                tetromino.rotate()
            elif event.key == K_LEFT:
                tetromino.shift(-1)
            elif event.key == K_RIGHT:
                tetromino.shift(1)

    # check game over condition
    if tetromino.game_over:
        text_with_bg(text="GAME OVER", text_color=RED, size=80,
                     pos=(WIDTH/2, HEIGHT/2), bg_color=WHITE, screen=screen)

    else:
        # shift tetromino
        tetromino.drop()
        if tetromino.is_landed:
            tetromino.lock_tetromino()
            score += matrix.line_clear()
            text_with_bg(text=str(score), text_color=BLACK, size=100, 
                        pos=(50, 50), bg_color=GREY, screen=screen)

    # draw display
    py.display.update()
