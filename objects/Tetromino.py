import pygame as py
from constants import *
from objects.Mino import Mino
import random

class Tetromino:
    def __init__(self, screen, grid, background):
        self.screen = screen
        self.background = background
        self.grid = grid
        self.drop_wait = 100
        self.reset()

    def reset(self):
        self.grid_pos = (int(MINO_WID / 2) - 2, 1)
        self.rotations, self.color = self.get_rand_shape()
        self.rot_idx = 0
        self.matrix = self.get_matrix(self.rot_idx, self.grid_pos)

        self.minos = [Mino(self.color, pos, self.screen, self.background) for pos in self.matrix]

    def draw(self):
        for m in self.minos:
            m.draw()

    def rotate(self):
        self.rot_idx = (self.rot_idx + 1) % len(self.rotations)
        self.matrix = self.get_matrix(self.rot_idx, self.grid_pos)
        for i in range(4):
            new_pos = (self.matrix[i][0], self.matrix[i][1])
            self.minos[i].set_pos(new_pos)

        self.draw()

    def collision_check(self):
        pass

    def get_rand_shape(self):
        choice = random.choice(tetromino_attrs)
        return (choice.rotations, choice.color)

    def get_matrix(self, rot_idx, pos):
        "EX: [(0,1), (1,1), (0,2), (1,2)]"
        matrix = []
        for i in range(4):
            x_pos = self.rotations[rot_idx][i][0] + pos[0]
            y_pos = self.rotations[rot_idx][i][1] + pos[1]
            matrix.append((x_pos, y_pos))
        return matrix
    
