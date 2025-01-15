from constants import *

class Matrix:
    def __init__(self):
        self.grid = [[None] * MINO_WID for i in range(MINO_HGT)]
        print(self.grid)
            
    def line_clear(self):
        # clear out filled rows
        for r in range(MINO_HGT):
            if None not in self.grid[r]:
                print(f"full grid on row: {r}")
                self.clear(r)

        # shift rows down
        self.shift_rows()
                
    def clear(self, row):
        for mino in self.grid[row]:
            mino.clear()
        self.grid[row] = [None] * 10

    def shift_rows(self):
        pass