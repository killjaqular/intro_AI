import csv

from table import Table

"""
Converts input from a tab-seperated value to a Table

:param file_name: Name of the tab-seperated file
:return: A Table object containing all of the information
"""
def get_input(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        l = []
        for row in reader:
            l.append(row)
        return Table.create_table(l[0], l[1:])
