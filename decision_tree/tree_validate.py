"""
author      : Adonay Pichardo
description : Validation of provided tree
"""

# Standard Imports
from sys import stdout

class ConfusionMatrix:
    def __init__(self):
        self.outter_list = [[0.0, 0.0], [0.0, 0.0]]

    def __str__(self):
        string_representation = ''
        string_representation += f'\nConfusion Matrix\n'
        string_representation += f'╭--T-----F--╮\n'
        string_representation += f'T {self.outter_list[0][0]} | {self.outter_list[0][1]} |\n'
        string_representation += f'F {self.outter_list[1][0]} | {self.outter_list[1][1]} |\n'
        string_representation += f'╰--T-----F--╯\n'
        return string_representation

def tree_validate(given_tree, given_table):
    """
    tree_validate: xxx

    INPUT:         given_tree  - tree,  Decision Tree to traverse.
                   given_table - table, Table of original data.

    OUTPUT:        complete_confusion_matrix - ConfusionMatrix, Contains the count of
                                               True and False for each node in tree.
    """

    complete_confusion_matrix = ConfusionMatrix()

    stdout.write(f'tree_validate() START\n')
    stdout.write(f'given_tree\n{given_tree}\n')
    stdout.write(f'given_table\n{given_table}\n')
    stdout.write(f'tree_validate() STOP \n\n')

    return complete_confusion_matrix
