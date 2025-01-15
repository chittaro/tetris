import pygame as py
from constants import *


class Mino():
    def __init__(self, color, pos):
        self.dims = (MINO_SIZE, MINO_SIZE)
        self.color = color
        self.rect = py.Rect((pos[0] * MINO_SIZE, pos[1] * MINO_SIZE), self.dims) 

    def set_pos(self, pos):
        self.rect.update((pos[0] * MINO_SIZE, pos[1] * MINO_SIZE), self.dims)

    def draw(self, screen):
        py.draw.rect(screen, self.color, self.rect)

    def clear(self, screen, bg):
        screen.blit(bg, self.rect, self.rect)