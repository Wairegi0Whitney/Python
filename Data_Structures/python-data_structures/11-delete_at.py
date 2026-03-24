"""
Write a function that deletes the item at a specific position in a list.


Prototype: def delete_at(my_list=[], idx=0):



If idx is negative or out of range, nothing change (returns the same list)

You are not allowed to use pop()

You are not allowed to import any module
"""
def delete_at(my_list=[], idx=0):
    range=len(my_list)
    if idx>=range or idx<0:
        print(my_list)
    else:
        del my_list[idx]
        print(my_list)
    
list=[2,5,8,9,6]    
delete_at(list,idx=1)