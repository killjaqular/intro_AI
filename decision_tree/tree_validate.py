"""
author      : Adonay Pichardo
description : Validation of provided tree
"""

# Standard Imports
from sys import stdout

# Internal Imports
from tree_inference import tree_inference

class ConfusionMatrix:
    def __init__(self):
        self.matrix =\
        {
            (True,  True)  : 0,
            (True,  False) : 0,
            (False, True)  : 0,
            (False, False) : 0
        }
        self.total_count = 0

    def __str__(self):
        TT = self.matrix[(True,  True)]  / self.total_count
        TF = self.matrix[(True,  False)] / self.total_count
        FT = self.matrix[(False, True)]  / self.total_count
        FF = self.matrix[(False, False)] / self.total_count

        string_representation = ''
        string_representation += f'\nConfusion Matrix\n'
        string_representation += f'╭--T-----F--╮\n'
        string_representation += f'T {int(TT*100):02}% | {int(TF*100):02}% |\n'
        string_representation += f'F {int(FT*100):02}% | {int(FF*100):02}% |\n'
        string_representation += f'╰--T-----F--╯\n'
        return string_representation

    def record(self, entry):
        self.matrix[entry] += 1

def tree_validate(tree, table, actuals):
    """
    tree_validate: xxx

    INPUT:         tree  - tree,  Decision Tree to traverse.
                   table - table, Table of original data.

    OUTPUT:        complete_confusion_matrix - ConfusionMatrix, Contains the count of
                                               True and False for each node in tree.
    """

    complete_confusion_matrix = ConfusionMatrix()

    for every_row in table.get_rows():
        infered = tree_inference(tree, every_row)
        actual  = every_row.get_target()
        complete_confusion_matrix.total_count += 1
        complete_confusion_matrix.matrix[(infered, actual)] += 1

    return complete_confusion_matrix
