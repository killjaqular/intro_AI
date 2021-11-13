from decision_tree import DecisionTree
from table import Table

"""
Takes a table and creates a DecisionTree using the learning algorithm from the book

:param table: The Table object that we want to learn from
:return: A DecisionTree that is the result of the Table
"""
def tree_learn(table, default=False):
    # Deals with case where there are no rows
    if table.is_empty():
        return DecisionTree.create_leaf(default)
    # Handles case where all targets are the same
    if table.all_target_same():
        return DecisionTree.create_leaf(table.get_rows()[0].get_target())
    # Handles case where all attributes have been considered
    if len(table.get_attributes()) == 0:
        return DecisionTree.create_leaf(table.get_target_mode())

    best_attribute = choose_attribute(table)  # TODO: Create this function
    children = {}
    for val in table.get_attribute_values(best_attribute):
        new_table = Table.new_table_from_old(table, best_attribute, val)
        subtree = tree_learn(new_table, table.get_target_mode())
        children[val] = subtree

    return DecisionTree.create_attribute_node(best_attribute, children)

# TODO: Create real function
def choose_attribute(table):
    return table.get_attributes()[0]
