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
from get_input      import get_input as create_table
from tree_learn     import *
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
def verify_argv(argv):
    if len(argv) != 2:
        stdout.write(f'USAGE: user@host#_:> {argv[0]} <input_table>')
        exit()
# <Functions End>

# <Main Start>
def main():
    verify_argv(argv)

    table            = create_table(argv[1])
    tree             = tree_learn(table)

    # Alt,Bar,Fri,Hun,Pat,Price,Rain,Res,Type,Est
    # T,F,F,T,Some,$$$,F,T,French,0-10,T
    test =\
    {
        'Alt'   : 'T',
        'Bar'   : 'F',
        'Fri'   : 'F',
        'Hun'   : 'T',
        'Pat'   : 'Some',
        'Price' : '$$$',
        'Rain'  : 'F',
        'Res'   : 'T',
        'Type'  : 'French',
        'Est'   : '0-10'
    }

    for every_row in table.get_rows():
        inference_result = tree_inference(tree, every_row)

    # confusion_matrix = tree_validate(tree, table)
# <Main End>

if __name__ == '__main__':
    main()
