'''
rooted_tree.py

General data tree

Input is given as parent, chidren pairs
Example:
A,BC
B,DE
C,FG
D,HI
E,JK
F,LM
G,NO

'''
#REQUIRED LIBRARIES
###################################################################################################
from sys import argv, stdin, stdout

#OBJECTS/CLASSES
###################################################################################################
class Node:
    def __init__(self, new_element):
        self.data     = new_element # The element stored in the node
        self.parent   = None        # Points to the parent of the node
        self.children = []          # List of the children of the node

#DEFINED FUNCTIONS
###################################################################################################
def readParentChildrenPair():
    line = stdin.readline()

    if line == '':
        return line

    stdout.write(f'{line}')

    return line.rstrip().split(',')

def printBFS(node):
    # if node is None: return

    # queue = [node]

    # while queue:
    #     node = queue.pop(0)

    #     stdout.write(f'{node.data}\n')

    #     if len(node.children) > 0: queue.extend(node.children)

    #     for every_child in node.children:
    #         stdout.write(f'{every_child.data} ')

    stdout.write(f'{node.data}\n')
    stdout.write(f'{node.children[0].data}')
    stdout.write(f'{node.children[1].data}')

def main():

    # Verify argv
    if len(argv) != 1:
        stdout.write(f'Missing argv[1]. Usage:_> {argv[0]} < input.file\n')
        return -1

    # Initialize any data structures needed
    root  = None
    queue = []

    # Run program
    while True:
        line = readParentChildrenPair()

        # If line is '', readline has read to the end of the file and we can exit while-loop
        if line == '':
            break

        ################################
        # Build nodes
        ################################
        new_node = Node(line[0])

        if root is None: root = new_node
        queue.append(root)

        for every_child in line[1]:
            new_child = Node(every_child)
            queue.append(new_child)

        current_node = queue.pop(0)
        while queue:
            for every_node in queue:
                current_node.children.append(every_node)

            line = readParentChildrenPair()

            # If line is '', readline has read to the end of the file and we can exit while-loop
            if line == '':
                break

            for every_child in line[1]:
                new_child = Node(every_child)
                queue.append(new_child)

            current_node = queue.pop(0)

    stdout.write('\n')

    printBFS(root)

#START PROGRAM
###################################################################################################
if __name__ == "__main__":
    main()
#END PROGRAM
