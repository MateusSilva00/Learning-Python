import turtle
import time
import sys
from collections import deque

window = turtle.Screen()
window.bgcolor("black")
window.title("Breadth Search vs Depth Search")
window.setup(800, 450)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Title(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("white")
        self.speed(0)

class Toy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green", "black")
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

class Purple(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)


graph = [
    "            -             ",
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

def makeMaze(graph):
    global startX, startY, endX, endY
    for j in range(len(graph)):
        for i in range(len(graph[j])):
            char = graph[j][i]
            screenX = -300 + (i * 24)
            screenY = 150 - (j * 24)

            if char == '-':
                title.hideturtle()
                title.goto(screenX, screenY)

            if char == '+':
                maze.goto(screenX, screenY)
                maze.stamp()
                walls.append((screenX, screenY))

            if char == ' '  or char == 'g':
                path.append((screenX, screenY))
                if char == 'g':
                    purple.goto(screenX, screenY)
                    purple.stamp()
                    endX, endY = screenX, screenY

            if char == 's':
                startX, startY = screenX, screenY
                red.goto(screenX, screenY)            
            
def endProgram():
    window.exitonclick()
    sys.exit()

def breadthSearch(x, y):
    title.write("Breadth First Search", align="center", font=("Arial", 12, "bold"))
    frontier.append((x, y))
    solution[x, y] = x, y
    goal = endX, endY
    while len(frontier) > 0  or goal not in visited:
        time.sleep(0)
        x, y = frontier.popleft()

        # Verifica cédulas à esquerda
        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x-24, y))

        # Verifica cédulas à abaixo
        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))

        # Verifica cédulas à direita
        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x + 24, y))

        # Verifica cédulas à acima
        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        toy.goto(x, y)
        toy.stamp()

def depthSearch(x, y):
    title.write("Depth First Search", align="center", font=("Arial", 12, "bold"))
    frontier.append((x, y))
    solution[x, y] = x, y
    goal = endX, endY

    while len(frontier) > 0 and goal not in visited:
        time.sleep(0)
        x, y = frontier.pop()

        if (x - 24, y) in path and (x - 24,  y) not in visited:
            visited.add((x-24, y))
            cell = (x - 24, y)
            solution[cell] = x, y
            frontier.append(cell)

        if (x + 24, y) in path and (x + 24, y) not in visited:
            visited.add((x + 24, y))
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)

        if (x, y + 24) in path and (x, y + 24) not in visited:
            visited.add((x, y + 24))
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            visited.add((x, y - 24))
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
        
        toy.goto(x, y)
        toy.stamp()


def wayHome(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (startX, startY):   
        yellow.goto(solution[x, y])       
        yellow.stamp()
        x, y = solution[x, y] 


def clearMaze():
    time.sleep(2)
    toy.clear()
    yellow.clear()
    visited.clear()
    frontier.clear()
    solution.clear()
    title.clear()
    

if __name__ == "__main__":
    maze = Maze()
    title = Title()
    red = Red()
    toy = Toy()
    yellow = Yellow()
    purple = Purple()

    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}

    makeMaze(graph)
    breadthSearch(startX, startY)
    wayHome(endX, endY)
    clearMaze()
    time.sleep(3)

    depthSearch(startX, startY)
    wayHome(endX, endY)
    endProgram()
