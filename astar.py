'''
astar.py

A* algorithm implementation.
'''

#REQUIRED LIBRARIES
###################################################################################################
from sys import argv, stderr, stdin, stdout

#OBJECTS/CLASSES
###################################################################################################
class grid:
    grid  = [[]]
    x = None
    y = None

    def insert_cell(self, new_cell, x, y):
        self.grid[x][y] = new_cell

    def __init__(self):
        self.x = 0
        self.y = 0

class cell:
    x        = None
    y        = None
    distance = None
    visited  = None

class visitor:
    x                 = None
    y                 = None
    distance_traveled = None
    distance_left     = None
    distance_total    = None

class priority_queue:
    cells = []

    def enque(self, new_visitor):
        for index, every_visitor in enumerate(self.cells):
            if new_visitor.distance_total < every_visitor.distance_total and\
               new_visitor.x < every_visitor.x:
                self.cells.insert(index + 1, new_visitor)

    def deque(self):
        return self.cells.pop(0)

#DEFINED FUNCTIONS
###################################################################################################
def main():

    grid_ins = grid()

    # Read input
    for every_line in stdin.readlines():
        if grid_ins.x == 0:
            grid_ins.x = len(every_line) - 1
        grid_ins.y += 1

        for every_cell in every_line.rstrip():
            stdout.write(f'{every_cell}')

        stdout.write(f'\n')

#START PROGRAM
###################################################################################################
if __name__ == "__main__":
    main()
#END PROGRAM
