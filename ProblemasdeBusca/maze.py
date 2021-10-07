from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random 
from math import sqrt
from genericSearch import dfs, bfs, nodePath, astar, Node

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    cloumn: int