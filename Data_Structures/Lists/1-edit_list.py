mylist = ["apple", "banana", "cherry", "grapes","pineappe","avocado", "melon", "lemon"]
#Change Item Value
#change 3rd item
mylist[2]="Mango"
print(mylist)

#change a range of items
mylist[2:5]=["new_cherry", "new_grapes", "new_pineapple"]
print(mylist)

#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
mylist.insert(3,"inserted_oranges")
print(mylist)

#To add an item to the end of the list, use the append() method:
mylist.append("app_kiwi")
print(mylist)

#To append elements from another list to the current list, use the extend() method.
veggies=["spinach", "carrot", "cabbage"]
mylist.extend(veggies)
print(mylist)

#The remove() method removes the specified item.
mylist.remove("apple")
print(mylist)

#The pop() method removes the specified index.
#If you do not specify the index, the pop() method removes the last item.
mylist.pop(1)
print(mylist)

#The del keyword also removes the specified index:
del mylist[1]
print(mylist)