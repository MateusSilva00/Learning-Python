import turtle
import time
import sys
from collections import deque

window = turtle.Screen()
window.bgcolor("black")
window.title("A Breadth First Search for Maze Solving")
window.setup(800, 800)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid = [
    "++++++++++++++++++++++++++",
    "+s+           +++++++    +",
    "+ +                      +",
    "+ +       ++++   ++  +++++",
    "+ +       +              +",
    "+ +       ++++    +      +",
    "+ +     +++       +    +++",
    "+                 +   + g+",
    "+++++++           +     ++",
    "++++++       ++++++      +",
    "+                        +",
    "++++++++++++++++++++++++++",
]

def makeMaze(grid):
    global startX, startY, endX, endY
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            char = grid[i][j]
            screenX = -188 + (i * 24)
            screenY = 288 - (j * 24)

            if char == '+':
                maze.goto(screenX, screenY)
                maze.stamp()
                walls.append((screenX, screenY))

            if char == ' '  or char == 'e':
                path.append((screenX, screenY))
            
            if char == 'g':
                green.color("purple")
                green.goto(screenX, screenY)
                endX, endY = screenX, screenY
                green.stamp()
                green.color("green")
            
            if char == 's':
                startX, startY = screenX, screenY
                red.goto(screenX, screenY)            
            

def endProgram():
    window.exitonclick()
    sys.exit()


def breadthSearch(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        time.sleep(0)
        x, y = frontier.popleft()

        if(x - 24, y) in path and (x - 24, y) not in visited:  
            cell = (x - 24, y)
            solution[cell] = x, y
            frontier.append(cell)  
            visited.add((x-24, y)) 

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))

        if(x + 24, y) in path and (x + 24, y) not in visited:   
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x + 24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def wayHome(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (startX, startY):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]

if __name__ == "__main__":
    maze = Maze()
    red = Red()
    green = Green()
    yellow = Yellow()

    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}

    makeMaze(grid)
    breadthSearch(startX, startY)
    # wayHome(endX, endY)
    endProgram()
