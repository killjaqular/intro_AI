"""
author :      Adonay Pichardo
description : Validation of provided tree
"""

# Standard Imports
from sys import stdout

class ConfusionMatrix:
    def __init__(self):
        self.outter_list = []

    def insert_new_list(self):
        self.outter_list.append(list())

def tree_validate(given_tree, given_table):
    """
    tree_validate: xxx

    INPUT:         given_tree      - tree, xxx
                   given_table     - table, xxx

    OUTPUT:        ConfusionMatrix - ConfusionMatrix, xxx
    """

    complete_confusion_matrix = ConfusionMatrix()

    stdout.write(f'tree_validate() START\n')
    stdout.write(f'given_tree\n{given_tree}\n')
    stdout.write(f'given_table\n{given_table}\n')
    stdout.write(f'tree_validate() STOP \n\n')

    return complete_confusion_matrix
