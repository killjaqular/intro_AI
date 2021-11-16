"""
author      : Ian Orzel
description : Implements a data structure for storing a decision tree
"""

class DecisionTree:

    """
    Creates a basic DecisionTree instance. Should be private

    :param leaf: Whether or not the node is a leaf node
    :param bool: If it is a leaf node, has its boolean value
    :param children: A dictionary that maps the attribute value to a subtree
    :param attribute: A string of the attribute name
    :return: A DecisionTree object with these parameters set
    """
    def __init__(self, leaf=False, bool=False, children={}, attribute=""):
        self.leaf = leaf
        self.bool = bool
        self.children = children
        self.attribute = attribute

    def __str__(self):
        if self.leaf:
            return f'{self.bool}\n'
        else:
            s = f'{self.attribute}\n'
            for val in self.children.keys():
                s += f'{val}:\n'
                s += "     " + str(self.children[val]).replace("\n", "\n     ")[:-5]
            return s

    """
    Creates a DecisionTree for a leaf node

    :param bool: The boolean value of the leaf node
    :return: A DecisionTree object
    """
    @staticmethod
    def create_leaf(bool):
        return DecisionTree(leaf=True, bool=bool)

    """
    Creates a DecisionTree for an attribute node

    :param attribute: The string representing what attribute the node is related to
    :param children: A dictionary that maps string attribute values to other trees
    :return: A DecisionTree object
    """
    @staticmethod
    def create_attribute_node(attribute, children):
        return DecisionTree(attribute=attribute, children=children)

    """
    Determines whether the current node is a leaf

    :return: A boolean thats true if the node is a leaf
    """
    def is_leaf(self):
        return self.leaf

    """
    Returns the bool value of a leaf node

    :return: The boolean value of a leaf node
    """
    def get_bool(self):
        assert self.is_leaf()
        return self.bool

    """
    Returns the attribute of an attribute node

    :return: String of the attribute
    """
    def get_attribute(self):
        assert not self.is_leaf()
        return self.attribute

    """
    Returns the children of this node

    :return: a dictionary that links attribute strings to trees
    """
    def get_children(self):
        assert not self.is_leaf()
        return self.children
