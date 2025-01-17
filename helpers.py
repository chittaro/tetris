import pygame as py
from pygame.locals import *
from constants import *

def draw_lines(screen):
    for i in range(1, MINO_HGT + 1):
        y = i * MINO_SIZE - 1
        py.draw.line(screen, DARK_GREY, (0, y), (WIDTH, y), 2)
    for i in range(1, MINO_WID + 1):
        x = i * MINO_SIZE
        py.draw.line(screen, DARK_GREY, (x, 0), (x, HEIGHT), 2)
