from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random 
from math import sqrt
from genericSearch import dfs, bfs, nodeToPath, Node

class Cell(str, Enum):
    EMPTY = "   "
    BLOCKED = " X "
    START = " S "
    GOAL = "[ ]"
    PATH = " * "

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows = 10, columns = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0,0), goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows = rows
        self._columns = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # Preencher a grade com células vazias
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # Preencher a grade com células bloqueadas
        self.randomlyFill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL


    def randomlyFill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output
    
    def goalTest(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    
    def sucessors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1)) 
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path):
        for mazeLocation in path:
            self._grid[mazeLocation.row][mazeLocation.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def clear(self, path):
        for mazeLocation in path:
            self._grid[mazeLocation.row][mazeLocation.column] = Cell.EMPTY
        self._grid[self.start.row][mazeLocation.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    solution1 = dfs(maze.start, maze.goalTest, maze.sucessors)

    if solution1 is None:
        print("No solution find using depth-first search")
    else:
        path1 = nodeToPath(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)
    

    solution2 = bfs(maze.start, maze.goalTest, maze.sucessors)
    if solution2 is None:
        print("No solution found using breadth-first search")
    else:
        path2 = nodeToPath(solution2)
        maze.mark(path2) 
        print(maze)