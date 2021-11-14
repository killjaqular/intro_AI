# <Document_Header Start>
"""
filename : tree_validate.py
author : Adonay Pichardo
description :
Validation of provided tree
"""
# <Document_Header End>

# <Standard Imports Start>
from sys import stdout
# <Standard Imports End>

# <Internal Imports Start>
# <Internal Imports End>

# <External Imports Start>
# <External Imports End>

# <Global Objects Start>
# <Global Objects End>

# <Classes Start>
class ConfusionMatrix:
    def __init__(self):
        self.outter_list = []

    def insert_new_list(self):
        self.outter_list.append(list())
# <Classes End>

# <Functions Start>
def tree_validate(given_tree, given_table):
    """
    tree_validate: xxx
    INPUT:          given_tree      - tree, xxx
                    given_table     - table, xxx
    OUTPUT:         ConfusionMatrix - ConfusionMatrix, xxx
    """

    complete_confusion_matrix = ConfusionMatrix()

    stdout.write(f'tree_validate() START\n')
    stdout.write(f'given_tree\n{given_tree}\n')
    stdout.write(f'given_table\n{given_table}\n')
    stdout.write(f'tree_validate() STOP \n\n')

    return complete_confusion_matrix
# <Functions End>

# <Main Start>
# tree_validate should never be ran as a stand alone
# <Main End>
