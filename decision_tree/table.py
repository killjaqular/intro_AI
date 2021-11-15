"""
author      : Ian Orzel
description : ???
"""

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
        self.target = target

    def __str__(self):
        s = ""
        for attr in self.dict:
            s += f'{self.dict[attr]:<10}'
        s += "\n"
        return s


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
        return TableRow(dict=dict, target=(True if values[-1] == "T" else False))

    """
    Creates a new table row by taking out a row from an old one

    :param row: The old table row
    :param attribute: The attribute value being considered
    :return: A new TableRow object with the modifications
    """
    @staticmethod
    def create_row_from_old(row, attribute):
        # Copy over the values
        dict = {}
        for attr in row.get_attributes():
            if attr != attribute:
                dict[attr] = row.get_attribute_value(attr)
        target = row.target

        return TableRow(dict=dict, target=target)

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
    :param attr_vals: A dictionary that maps attribute names to sets of their values
    :return: A new Table object
    """
    def __init__(self, attributes, rows, attr_vals):
        self.attributes = attributes
        self.rows = rows
        self.attr_vals = attr_vals

    def __str__(self):
        s = ""
        for attr in self.attributes:
            s += f'{attr:<10}'
        s += "\n"
        for child in self.rows:
            s += str(child)
        return s

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

        attr_vals = {}
        for attr in attributes:
            attr_vals[attr] = set()
        for row in rows:
            for attr in attributes:
                attr_vals[attr].add(row.get_attribute_value(attr))

        return Table(attributes, rows, attr_vals)

    """
    Creates a new Table from an old table that have a certain value of an attribute

    :param table: The old table being modified
    :param attribute: The attribute being taken out
    :param value: The value of the attribute that will be taken
    :return: A new Table object
    """
    @staticmethod
    def new_table_from_old(table, attribute, value):
        # Creating the new list of attributes
        attributes = []
        for attr in table.get_attributes():
            if attr != attribute:
                attributes.append(attr)

        # Creating a new list of rows
        rows = []
        for row in table.get_rows():
            if row.get_attribute_value(attribute) == value:
                rows.append(TableRow.create_row_from_old(row, attribute))

        return Table(attributes, rows, table.attr_vals)

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

    """
    Gets a set of all possible values of an attribute

    :param attribute: String name of the attribute
    :return: A set of all possible values for the attribute
    """
    def get_attribute_values(self, attribute):
        return self.attr_vals[attribute]

    """
    Returns whether the table is empty

    :return: True if the table is empty, false otherwise
    """
    def is_empty(self):
        return len(self.get_rows()) == 0

    """
    Checks whether all rows have the same target value

    :return: True if all rows have the same target, False otherwise
    """
    def all_target_same(self):
        if self.is_empty():
            return True
        value = self.get_rows()[0].get_target()
        for i in range(1, len(self.get_rows())):
            if value != self.get_rows()[i].get_target():
                return False
        return True

    """
    Gets that mode of all target values

    :return: Returns a boolean value that occurs the most in the rows
    """
    def get_target_mode(self):
        trues = 0
        falses = 0
        for row in self.get_rows():
            if row.target:
                trues += 1
            else:
                falses += 1
        # Defaults to True
        return trues >= falses

    """
    Counts the number of times that the target is true and false when an attribute is at a specified value

    :param attribute: The attribute being examined
    :param value: The attribute value being counted
    :return: The number of trues and falses that occur
    """
    def count_vals(self, attribute, value):
        trues = 0
        falses = 0
        for row in self.get_rows():
            if row.get_attribute_value(attribute) == value:
                if row.get_target():
                    trues += 1
                else:
                    falses += 1
        return trues, falses

    """
    Creates a new table by leaving out one row

    :param row_num: The row number that we are leaving out
    :return: The table with the row left out and the row being left out
    """
    def leave_one_out(self, row_num):
        old_row = self.get_rows()[row_num]
        new_row_list = []
        for i in range(len(self.get_rows())):
            if i != row_num:
                new_row_list.append(self.get_rows()[i])
        return Table(self.attributes, new_row_list, self.attr_vals), old_row
