import pygame as py
from pygame.locals import *
from objects.Matrix import Matrix
from objects.Tetromino import Tetromino
from objects.Text import *
from constants import *
import time

# Initialize game & clock
py.init()
py.font.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Tetris")
clock = py.time.Clock()

# Initialize & blit background
background = py.Surface(screen.get_size()).convert()
background.fill((200, 200, 200))
screen.blit(background, (0, 0))
py.display.flip()

# Initialize Matrix (grid)
matrix = Matrix()

# Initialize Tetromino
tetromino = Tetromino(screen, matrix.grid, background)

score = 9
render_with_bg(str(score), (0,0,0), 200, (WIDTH/2, HEIGHT/2), (200,200,200), screen)

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
        print("GAME OVER")
        time.sleep(2)
        running = False

    # shift tetromino
    tetromino.drop()
    if tetromino.is_landed:
        tetromino.lock_tetromino()
        score += matrix.line_clear()
        render_with_bg(text=str(score), text_color=(0,0,0), size=100, 
                       pos=(50, 50), bg_color=(200,200,200), screen=screen)

    # draw display
    py.display.update()
