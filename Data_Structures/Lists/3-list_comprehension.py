MyList=["mango","orange","apple"]

#you want n new list, containing only the fruits with the letter "n" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
NewList=[]
for x in MyList:
    if "n" in x:
        NewList.append(x)
print(NewList)


#With list comprehension you can do all that with only one line of code:
NewList=[x for x in MyList if "n" in x]
print(NewList)

#print the fruits but do not print apple
NewList=[x for x in MyList if x!="apple"]
print(NewList)