"""
A row of the table, representing a particular example
"""
class TableRow():
    """
    Creates a new TableRow object (Should be private)

    :param dict: Dictionary that maps an attribute to its value
    :param target: The target value for this row
    :return: A new TableRow
    """
    def __init__(self, dict={}, target=False):
        self.dict = dict
        self.value = value

    """
    Creates a new TableRow object

    :param attributes: A list of all attributes
    :param values: A list of all attribute values in the order of the attributes with the last value being the target
    :return: A new TableRow object
    """
    @staticmethod
    def create_row(attributes, values):
        dict = {}
        for i in range(len(attributes)):
            dict[attributes[i]] = values[i]
        return TableRow(dict=dict, target=values[-1])

    """
    Gets a list of attributes associated with the row

    :return: A list object containing all the strings of attributes
    """
    def get_attributes(self):
        return self.dict.keys()

    """
    Gets the value for a particular attribute assuming that the attribute is a part of the row

    :param attribute: The string of the attribute considered
    :return: The string value of that attribute
    """
    def get_attribute_value(self, attribute):
        assert attribute in self.get_attributes()
        return self.dict[attribute]

    """
    Gets the value of the target for the row

    :return: The target value
    """
    def get_target(self):
        return self.target

"""
A table, which is a list of TableRows
"""
class Table():
    pass
