"""
Write a function that removes all characters c and C from a string.


Prototype: def no_c(my_string):



The function should return the new string

You are not allowed to import any module

You are not allowed to use str.replace()
"""

def no_c(my_string):
    new_string=""
    for x in my_string:
        if x!="c"and"C":
            new_string+=x
    print(new_string)

Name="coconut"
no_c(Name)
