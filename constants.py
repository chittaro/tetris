WIDTH = 500
HEIGHT = 900
MINO_SIZE = 50
MINO_WID = int(WIDTH / MINO_SIZE)
MINO_HGT = int(HEIGHT / MINO_SIZE)

class Attributes:
    def __init__(self, rotations, color):
        self.rotations = rotations
        self.color = color

# defines relative positioning of top left
# coordinatess of Minos within bounds block
tetromino_attrs = [
    Attributes( #I
        rotations=[[(0,2), (1,2), (2,2), (2,3)], [(2,0), (2,1), (2,2), (3,2)]],
        color=(0, 240, 240)),
    Attributes( #O
        rotations=[[(1,1), (2,1), (2,2), (1,2)]],
        color=(241, 239, 47)),
    Attributes( #J
        rotations=[[(0,1), (1,1), (2,1), (2,2)], [(0,2), (1,2), (1,1), (1,0)], [(0,0), (0,1), (1,1), (2,1)], [(1,0), (2,0), (1,1), (1,2)]],
        color=(0, 0, 240)),
    Attributes( #L
        rotations=[[(0,1), (0,2), (1,1), (2,1)], [(0,0), (1,0), (1,1), (1,2)], [(0,1), (1,1), (2,1), (2,0)], [(1,0), (1,1), (1,2), (2,2)]],
        color=(221, 164, 34)),
    Attributes( #S
        rotations=[[(1,1), (2,1), (1,2), (0,2)], [(1,0), (1,1), (2,1), (2,2)]],
        color=(138, 234, 40)),
    Attributes( #T
        rotations=[[(0,1), (1,1), (2,1), (2,1)], [(0,1), (1,0), (1,1), (1,2)], [(0,1), (1,1), (1,0), (2,1)], [(1,0), (1,1), (2,1), (1,2)]],
        color=(136, 44, 237)),
    Attributes( #Z
        rotations=[[(0,1), (1,1), (1,2), (2,2)], [(1,1), (1,2), (2,1), (2,0)]],
        color=(207, 54, 22))
]