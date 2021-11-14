# <Document_Header Start>
"""
filename : tree_inference.py
author : Adonay Pichardo
description :
Inferencing from provided tree
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
# <Classes End>

# <Functions Start>
def tree_inference(given_tree, given_list):
    """
    tree_inference: xxx
    INPUT:          given_tree - tree, xxx
                    given_list - list, xxx
    OUTPUT:         True if xxx, else False
    """

    stdout.write(f'tree_inference() START\n')
    stdout.write(f'given_tree\n{given_tree}\n')
    stdout.write(f'given_list\n{given_list}\n')

    for every_attribute in given_list:
        stdout.write(f'infering {every_attribute}\n')

    stdout.write(f'tree_inference() STOP \n\n')

    return True
# <Functions End>

# <Main Start>
# tree_inference should never be ran as a stand alone
# <Main End>
