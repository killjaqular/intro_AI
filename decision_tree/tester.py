from decision_tree import *
from table import *
from get_input import *
from tree_learn import *
from tree_inference import *
from tree_validate import *

table = get_input("../input/main.in")
tree = tree_learn(table)
print(tree)
print("the row we are passing:_> " + str(table.get_rows()[1]))
print("tree_inference:_> " + str(tree_inference(tree, table.get_rows()[1])))

table1 = get_input("../input/extrainput1.in")
print(tree_validate(tree, table1))

table2 = get_input("../input/extrainput2.in")
print(tree_validate(tree, table2))
