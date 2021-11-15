"""
author      : Adonay Pichardo, Ian Orzel
description : Given the name of a file to open and read data from, learns table, infers,
              validates, and runs query on a Decision Tree.
"""

# Standard Imports
from sys import argv, stdout

# Internal Imports
from get_input      import get_input as create_table
from tree_learn     import *
from tree_inference import tree_inference
from tree_validate  import tree_validate

# <Functions Start>
def verify_argv(argv):
    if len(argv) != 2:
        stdout.write(f'USAGE: user@host#_:> {argv[0]} <input_table>')
        exit()
# <Functions End>

# <Main Start>
def main():
    verify_argv(argv)

    table = create_table(argv[1])
    stdout.write(f'Table:\n')
    stdout.write(f'{table}\n')

    tree  = tree_learn(table)
    stdout.write(f'Tree:\n')
    stdout.write(f'{tree}\n')

    stdout.write(f'\n<TREE INFERENCE>\n')
    for every_row in table.get_rows():
        stdout.write(f'Infering:\n')
        stdout.write(f'{every_row}\n')
        inference_result = tree_inference(tree, every_row)
        stdout.write(f'{inference_result}\n')

    stdout.write(f'\n<TREE VALIDATION>\n')
    confusion_matrix = tree_validate(tree, table)
    stdout.write(f'{confusion_matrix}')
# <Main End>

if __name__ == '__main__':
    main()
