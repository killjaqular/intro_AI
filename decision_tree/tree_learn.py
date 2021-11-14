from decision_tree import DecisionTree
from table import Table

from math import log

"""
Takes a table and creates a DecisionTree using the learning algorithm from the book

:param table: The Table object that we want to learn from
:return: A DecisionTree that is the result of the Table
"""
def tree_learn(table, default=True):
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

"""
Chooses the next attribute needed for building the tree

:param table: The Table that is being used to build the tree
:return: The attribute that should be turned into a node
"""
def choose_attribute(table):
    best_entropy = 2
    best_attribute = ""
    for attr in table.get_attributes():
        e = entropy_of_attribute(table, attr)
        if e < best_entropy:
            best_entropy = e
            best_attribute = attr
    return best_attribute

"""
Computes the entropy of a certain attribute

:param tabel: The Table being examined
:param attribute: The attribute whose entropy is being computed
:return: The entropy of that attribute
"""
def entropy_of_attribute(table, attribute):
    sum = 0
    for value in table.get_attribute_values(attribute):
        t, f = table.count_vals(attribute, value)
        if t + f != 0:
            sum += (t+f)/(len(table.get_rows())) * calc_entropy(t/(t+f), f/(t+f))
    return sum

"""
Computes the entropy value of two probabilities

:param p1: The first probability
:param p2: The second probability
:return: The double value of the entropy
"""
def calc_entropy(p1, p2):
    if p1 == 0 or p2 == 0:
        return 0
    return -p1*log(p1, 2) - p2*log(p2, 2)
