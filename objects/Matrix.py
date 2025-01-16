from constants import *

class Matrix:
    def __init__(self):
        self.grid = [[None] * MINO_WID for i in range(MINO_HGT)]
            
    def line_clear(self):
        # erase minos
        self.clear_minos()

        # clear out filled rows
        num_clears = 0
        for r in range(MINO_HGT):
            if None not in self.grid[r]:
                self.grid[r] = [None] * MINO_WID
                num_clears += 1
        # shift rows down
        self.shift_rows()

        # redraw minos
        self.draw_minos()

        return num_clears

    def shift_rows(self):
        # work upwards from bottom
        for i in range(MINO_HGT - 1, 1, -1):
            if self.grid[i] == [None] * MINO_WID:
                continue
            shift_pos = i
            while shift_pos + 1 < MINO_HGT and self.grid[shift_pos + 1] == [None] * MINO_WID:
                shift_pos += 1
            self.grid[shift_pos] = self.grid[i]
            if shift_pos - i > 0:
                self.grid[i] = [None] * MINO_WID
            self.shift_down_minos(shift_pos, shift_pos - i)

    def shift_down_minos(self, row, delta_y):
        for mino in self.grid[row]:
            if mino is not None:
                mino.shift_pos(0, delta_y)

    def clear_minos(self):
        for r in range(MINO_HGT):
            for c in range(MINO_WID):
                mino = self.grid[r][c]
                if mino is not None:
                    mino.clear()

    def draw_minos(self):
        for r in range(MINO_HGT):
            for c in range(MINO_WID):
                mino = self.grid[r][c]
                if mino is not None:
                    mino.draw()
