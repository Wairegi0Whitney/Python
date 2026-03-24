"""
Write a function that finds all multiples of 2 in a list.


Prototype: def divisible_by_2(my_list=[]):



Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2

The new list should have the same size as the original list

You are not allowed to import any module
"""
def divisible_by_2(my_list=[]):
    div=[]
    for value in my_list:
        if value%2==0:
            div.append(True)
        else:
            div.append(False)
    
    print(div)

list=[2,7,5,6,8,0,4]
divisible_by_2(list)