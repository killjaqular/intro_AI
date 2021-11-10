class DecisionTree:

    def __init__(self, leaf=False, bool=False, children={}, attribute=""):
        self.leaf = leaf
        self.bool = bool
        self.children = children
        self.attriute = attribute

    def create_leaf(self, bool):
        return DecisionTree(leaf=True, bool=bool)
    #TODO
