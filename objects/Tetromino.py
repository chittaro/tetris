import pygame as py
from constants import *
from objects.Mino import Mino
import random

class Tetromino:

    def __init__(self, screen, grid, background):
        self.screen = screen
        self.background = background
        self.grid = grid
        self.reset()

    def reset(self):
        self.grid_pos = [int(MINO_WID / 2) - 2, 0]
        self.rotations, self.color = self.get_rand_shape()
        self.rot_idx = 0
        self.waited = 0
        self.is_landed = False
        self.speed = 60
        self.drop_wait = self.speed
        matrix = self.get_matrix(self.rot_idx, self.grid_pos)
        self.minos = [Mino(self.color, pos, self.screen, self.background) for pos in matrix]
        self.ghost_minos = []
        # check game over condition
        if self.is_colliding(self.grid_pos, self.rot_idx):
            self.game_over = True
        else:
            self.game_over = False
            self.draw()
            self.draw_ghost_minos()

    def draw(self):
        for m in self.minos:
            m.draw()

    def toggle_speedy(self, is_speedy):
        if is_speedy:
            self.drop_wait = 5
        else:
            self.drop_wait = self.speed

    def update(self):
        self.waited += 1

    def inc_speed(self):
        self.speed -= 3
        self.drop_wait = self.speed

    def drop(self):
        # shift tetromino downwards after time interval        
        self.waited = 0
        temp_pos = [self.grid_pos[0], self.grid_pos[1] + 1]
        # shift downwards if possible
        if not self.is_colliding(temp_pos, self.rot_idx):
            self.grid_pos = temp_pos
            self.update_and_draw_minos()
        # lock tetromino
        else:
            self.is_landed = True

    def rotate(self):
        temp_rot = (self.rot_idx + 1) % len(self.rotations)
        # rotate if possible
        if not self.is_colliding(self.grid_pos, temp_rot):
            self.rot_idx = temp_rot
            self.update_and_draw_minos()
            self.draw_ghost_minos()
        
    def shift(self, delta_x):
        temp_pos = [self.grid_pos[0] + delta_x, self.grid_pos[1]]
        # shift L or R if possible
        if not self.is_colliding(temp_pos, self.rot_idx):
            self.grid_pos = temp_pos
            self.update_and_draw_minos()
            self.draw_ghost_minos()

    def lock_tetromino(self):
        # locks tetromino into grid upon drop conflict
        for m in self.minos:
            self.grid[m.get_pos()[1]][m.get_pos()[0]] = m

    def update_and_draw_minos(self):
        # update mino rects w/ new position/rotation
        matrix = self.get_matrix(self.rot_idx, self.grid_pos)
        for i in range(4):
            new_pos = (matrix[i][0], matrix[i][1])
            self.minos[i].set_pos(new_pos)
        self.draw()

    def is_colliding(self, pos, rot_idx):
        # check if any minos are in conflict
        matrix = self.get_matrix(rot_idx, pos)
        for vec in matrix:
            # check wall collision
            if vec[0] < 0 or vec[0] >= MINO_WID or vec[1] < 0 or vec[1] >= MINO_HGT:
                return True
            # check locked mino collision
            if self.grid[vec[1]][vec[0]] is not None:
                return True
        return False

    def get_rand_shape(self):
        # generate new tetromino shape
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
    
    def get_ghost_minos(self):
        temp_pos = [self.grid_pos[0], self.grid_pos[1]]
        while not self.is_colliding(temp_pos, self.rot_idx):
            temp_pos[1] += 1
        temp_pos[1] -= 1
        matrix = self.get_matrix(self.rot_idx, temp_pos)
        self.ghost_minos = [Mino(self.color, pos, self.screen, self.background) for pos in matrix]

    def draw_ghost_minos(self):
        for m in self.ghost_minos:
            m.clear()
        self.get_ghost_minos()
        for m in self.ghost_minos:
            m.draw(5)