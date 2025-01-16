import pygame as py
from constants import *


class Mino():
    def __init__(self, color, pos, screen, background):
        self.screen = screen
        self.background = background
        self.dims = (MINO_SIZE, MINO_SIZE)
        self.color = color
        self.rect = py.Rect((pos[0] * MINO_SIZE, pos[1] * MINO_SIZE), self.dims) 

    def set_pos(self, pos):
        self.clear()
        self.rect.update((pos[0] * MINO_SIZE, pos[1] * MINO_SIZE), self.dims)

    def shift_pos(self, delta_x, delta_y):
        self.clear()
        self.rect.move_ip(delta_x * MINO_SIZE, delta_y * MINO_SIZE)

    def get_pos(self):
        return [int(self.rect.x / MINO_SIZE), int(self.rect.y / MINO_SIZE)]

    def draw(self):
        py.draw.rect(self.screen, self.color, self.rect)

    def clear(self):
        self.screen.blit(self.background, self.rect, self.rect)