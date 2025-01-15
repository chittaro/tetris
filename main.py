import os, math, random
import pygame as py
from pygame.locals import *
from objects.Tetromino import Tetromino
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

# Initialize Grid
grid = [[None for i in range(MINO_WID)] for i in range(MINO_HGT)]

# Initialize Tetromino
tet = Tetromino(screen, grid, background)
tet.draw()

running = True
while running:
    clock.tick(60)

    for event in py.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                tet.rotate()
            elif event.key == K_LEFT:
                tet.shift(-1)
            elif event.key == K_RIGHT:
                tet.shift(1)

    tet.drop()
    py.display.update()
