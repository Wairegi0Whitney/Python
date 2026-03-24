"""
Write a function that finds the biggest integer of a list.


Prototype: def max_integer(my_list=[]):



If the list is empty, return None

You can assume that the list only contains integers

You are not allowed to import any module

You are not allowed to use the builtin max()

"""
def max_integer(my_list=[]):
    if len(my_list)==0:
        return None
    a=my_list[0]
    for i in my_list:
        if i > a:
            a=i
    print (a)

list=[2,8,9,0,78,5,6]
max_integer(list)