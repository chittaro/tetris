import pygame as py
from pygame.locals import *
from objects.Tetromino import Tetromino
from objects.Matrix import Matrix
from constants import *

# Initialize game & clock
py.init()
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

    tetromino.drop()
    if tetromino.is_landed:
        tetromino.lock_tetromino()
        matrix.line_clear()


    py.display.update()
