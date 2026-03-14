#Lists are used to store multiple items in a single variable.
#List is a collection which is ordered and changeable. Allows duplicate members.
mylist = ["apple", "banana", "cherry", "grapes","pineappe","avocado", "melon", "lemon"]
print(mylist)
print(mylist[2])
print(len(mylist))
print(type(mylist))

#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
print(mylist[2:])
print(mylist[3:6])

#To determine if a specified item is present in a list use the in keyword
names=["wairegi","whitney","jane","mary","joy","peace","rose","wanjiru"]
if "wanjiru" in names:
    print("name available")

    