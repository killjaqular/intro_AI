"""
A row of the table, representing a particular example
"""
class TableRow():
    """
    Creates a new TableRow object (Should be private)

    :param dict: Dictionary that maps an attribute to its value
    :return: A new TableRow
    """
    def __init__(self, dict={}):
        self.dict = dict

    pass

"""
A table, which is a list of TableRows
"""
class Table():
    pass
