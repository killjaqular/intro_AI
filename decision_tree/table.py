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
    """
    Creates a new Table object (Should be private)

    :param attributes: A list of all attribute names
    :param rows: A list of all TableRow objects in the table
    :return: A new Table object
    """
    def __init__(self, attributes, rows):
        self.attributes = attributes
        self.rows = rows

    """
    Creates a new Table object

    :param attributes: A list of the names of the attributes
    :param arr: A two dimensional array where each row has the attribute values and ends with the target
    :return: A new Table object
    """
    @staticmethod
    def create_table(attributes, arr):
        rows = []
        for a in arr:
            rows.append(TableRow.create_row(attributes, a))
        return Table(attributes, rows)

    """
    Gets a list of all the attributes in the table

    :return: A list of strings that are the attribute names
    """
    def get_attributes(self):
        return self.attributes

    """
    Gets a list of all the rows in the table

    :return: A list of TableRows
    """
    def get_rows(self):
        return self.rows
