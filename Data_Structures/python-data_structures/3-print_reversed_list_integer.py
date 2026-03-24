"""
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):

Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
"""

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))

num=[3,4,5,6,7]        
print_reversed_list_integer(num)
