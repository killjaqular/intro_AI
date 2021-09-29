'''
astar.py

A* algorithm implementation.
NOTE: Professor uses coordinate system in y,x pair instead of x,y
'''

#REQUIRED LIBRARIES
###################################################################################################
from sys import argv, stderr, stdin, stdout
from math import sqrt

#OBJECTS/CLASSES
###################################################################################################
class cell:
    x        = None
    y        = None
    distance = None
    symbol   = None

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.distance = sqrt(pow(x, 2) + pow(y, 2))
        self.symbol = symbol

class grid:
    grid  = []
    x            = None
    y            = None
    max_distance = None

    def __init__(self):
        self.x = 0
        self.y = 0

    def set_max_distance(self):
        self.max_distance = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def build_grid(self):
        current_y = 0
        # Read input
        for every_line in stdin.readlines():
            if self.x == 0:
                self.x = len(every_line) - 1
            self.y += 1

            current_x = 0
            self.grid.append([])
            for every_cell in every_line.rstrip():
                self.grid[current_y].append(cell(current_x, current_y, every_cell))
                current_x += 1
        
            current_y += 1

    def print(self):
        for every_row in self.grid:
            for every_cell in every_row:
                stdout.write(f'{every_cell.symbol}')
            stdout.write(f'\n')

class visitor:
    x             = None
    y             = None
    distance_left = None

    def __init__(self, cell, grid):
        self.x = cell.x
        self.y = cell.y
        self.distance_left = grid.max_distance - cell.distance

class priority_queue:
    cells = []

    def enque(self, new_visitor):
        for index, every_visitor in enumerate(self.cells):
            if every_visitor is not None:
                if new_visitor.distance_left < every_visitor.distance_left and\
                   new_visitor.x < every_visitor.x:
                    self.cells.insert(index + 1, new_visitor)

    def deque(self):
        return self.cells.pop(0)

    def print(self):
        for every_row in self.cells:
            for every_cell in every_row:
                stdout.write(f'<{every_cell.x}:{every_cell.y}>')
            stdout.write(f'\n')

#DEFINED FUNCTIONS
###################################################################################################
def a_star_search(grid):
    queue = priority_queue()

    for every_row in grid.grid:
        for every_cell in every_row:
            visitor_ins = visitor(every_cell, grid)
            queue.enque(visitor_ins)

    queue.print()

def main():

    grid_ins = grid()
    grid_ins.build_grid()
    grid_ins.set_max_distance()
    stdout.write(f'{grid_ins.max_distance}\n')
    grid_ins.print()

    a_star_search(grid_ins)

#START PROGRAM
###################################################################################################
if __name__ == "__main__":
    main()
#END PROGRAM
