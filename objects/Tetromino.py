import pygame as py
from constants import *
from objects.Mino import Mino
import random

class Tetromino:
    def __init__(self, screen, grid, background):
        self.screen = screen
        self.background = background
        self.grid = grid
        self.drop_wait = 50
        self.reset()

    def reset(self):
        self.grid_pos = [int(MINO_WID / 2) - 2, 1]
        self.rotations, self.color = self.get_rand_shape()
        self.rot_idx = 0
        self.waited = 0
        matrix = self.get_matrix(self.rot_idx, self.grid_pos)
        self.minos = [Mino(self.color, pos, self.screen, self.background) for pos in matrix]

    def draw(self):
        for m in self.minos:
            m.draw()

    def drop(self):
        self.waited += 1
        if self.waited >= self.drop_wait:
            self.waited = 0
            self.grid_pos[1] += 1
            self.update_and_draw_minos()

    def rotate(self):
        temp_rot = (self.rot_idx + 1) % len(self.rotations)
        if not self.is_colliding(self.grid_pos, temp_rot):
            self.rot_idx = temp_rot
            self.update_and_draw_minos()
        
    def shift(self, delta_x):
        temp_pos = [self.grid_pos[0] + delta_x, self.grid_pos[1]]
        if not self.is_colliding(temp_pos, self.rot_idx):
            print("shift success")
            self.grid_pos = temp_pos
            self.update_and_draw_minos()

    def update_and_draw_minos(self):
        matrix = self.get_matrix(self.rot_idx, self.grid_pos)
        for i in range(4):
            new_pos = (matrix[i][0], matrix[i][1])
            self.minos[i].set_pos(new_pos)
        self.draw()

    def is_colliding(self, pos, rot_idx):
        matrix = self.get_matrix(rot_idx, pos)
        for vec in matrix:
            # check wall collision
            if vec[0] < 0 or vec[0] >= MINO_WID or vec[1] < 0 or vec[1] >= MINO_HGT:
                print("can't shift: wall collision")
                return True
            # check locked mino collision
            if self.grid[vec[1]][vec[0]] is not None:
                print("can't shift: locked collision")
                return True
        return False

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
    
