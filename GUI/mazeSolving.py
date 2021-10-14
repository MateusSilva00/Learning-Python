from enum import Enum
import random
from typing import NamedTuple
from PIL import Image, ImageDraw

zoom = 20
borders = 6

class Cell(str, Enum):
    EMPTY = "0"
    BLOCKED = "1"
    START = "O"
    END = "[]"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows=10, columns = 20, start = MazeLocation(0, 0), end = MazeLocation(9, 19), sparseness = 0.2):
        self._rows = rows
        self._column = columns
        self.start = start
        self.end = end
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self.randomFill(rows, columns, sparseness)
        # self._grid[start.row][start.column] = Cell.START
        # self._grid[end.row][end.column] = Cell.END

    def randomFill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if row == 0 or row == 9:
                    self._grid[row][column] = Cell.BLOCKED
                if column == 0 or column == 19:
                    self._grid[row][column] = Cell.BLOCKED
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED
    
    def __str__(self) -> str:
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output
    
    def goalTest(self, ml: MazeLocation) -> bool:
        return ml == self.goal

def drawMatriz(a):
    im = Image.new("RGB", (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.show()

if __name__ == "__main__":
    a = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    maze = Maze()
    print(maze)
    drawMatriz(maze)
