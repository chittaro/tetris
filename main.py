import pygame as py
from pygame.locals import *
from objects.Matrix import Matrix
from objects.Tetromino import Tetromino
from objects.Text import render_text
from constants import *

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

# Initialize score
score_rect = py.Rect(10, 10, 50, 50)
score = 0
render_text(str(score), score_rect, (0, 0, 0), 50, background)

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

    # shift tetromino
    tetromino.drop()
    if tetromino.is_landed:
        tetromino.lock_tetromino()
        score += matrix.line_clear()
        screen.blit(background, score_rect, score_rect)
        render_text(str(score), score_rect, (0, 0, 0), 50, background)

    # draw text
    

    py.display.update()
