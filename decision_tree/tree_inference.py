"""
author :      Adonay Pichardo
description : Inference of provided tree
"""

# Standard Imports
from sys import stdout

def tree_inference(given_node, given_list):
    """
    tree_inference: For every attribute in given_list, we descend the tree
                    until a leaf given_node is reached in the Decision Tree.

    INPUT:          given_node - DecisionTree, A Decision Tree.
                    given_list - list,   The list of attributes to traverse through
                    the Decision Tree.

    OUTPUT:         The boolean stored in the Decision Tree when the leaf
                    given_node is reached. True, or False.
    """

    if given_node.is_leaf():
        result = given_node.get_bool()

    else:
        current_node_attribute = given_node.get_attribute()
        current_value          = given_list.get_attribute_value(current_node_attribute)
        child_to_follow        = given_node.get_children()[current_value]
        result = tree_inference(child_to_follow, given_list)

    return result
