# <Document_Header Start>
"""
filename : main.py
author : Adonay Pichardo
description :
Given the name of a file to open and read data from,
learns table, infers, validates, and runs query on a
Decision Tree.
"""
# <Document_Header End>

# <Standard Imports Start>
# List all imports alphabetically for Python3 standard libraries
from sys import argv, stdout
# <Standard Imports End>

# <Internal Imports Start>
# from create_table   import create_table
# from tree_learn     import tree_learn
from tree_inference import tree_inference
from tree_validate  import tree_validate
# <Internal Imports End>

# <External Imports Start>
# <External Imports End>

# <Global Objects Start>
# <Global Objects End>

# <Classes Start>
# <Classes End>

# <Functions Start>
def verify_argv():
    if len(argv) != 2:
        stdout.write(f'USAGE: user@host#_:> {argv[0]} <input_table>')
        exit()
# <Functions End>

# <Main Start>
def main():
    input_table      = open(argv[1], 'r')

    # table            = create_table()
    # tree             = tree_learn(table)
    table            = None
    some_list        = []
    tree             = None
    inference        = tree_inference(tree, some_list)
    confusion_matrix = tree_validate(tree, table)
# <Main End>

if __name__ == '__main__':
    main()