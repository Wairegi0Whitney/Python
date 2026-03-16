#Declare an empty list
list=[]

#Declare a list with more than 5 items
list=["kenya","uganda","ethiopia","tanzania","sudan","somalia"]

#Find the length of your list
len_list=len(list)
print(len_list)

#Get the first item, the middle item and the last item of the list
first_item=list[0]
mid_item=list[len(list)//2]
last_item=list[(len(list)-1)]
print("first_item: ",first_item)
print("mid_item: ",mid_item)
print("last_item: ",last_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["wairegi", 23, "single", "12 street Nairobi"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
first_company=it_companies[0]
mid_company=it_companies[len(list)//2]
last_company=it_companies[(len(list)-1)]
print("first_company: ",first_company)
print("mid_company: ",mid_company)
print("last_company: ",last_company)

#Print the list after modifying one of the companies
it_companies[0]="meta"
print(it_companies)

#Add an IT company to it_companies
it_companies.append("NVIDIA")
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert((len(list)//2),"SAP")
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
Upper=[x.upper() for x in it_companies if x!="IBM"]
print(Upper)

#Join the it_companies with a string '#;  '
hash=["#",]
it_companies.extend(hash)
print(it_companies)

#Check if a certain company exists in the it_companies list.

if "Amazon" in it_companies:
    print('company available')

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#Slice out the first 3 companies from the list
first_three= it_companies[:3]
print("first_three: ", first_three)

#Slice out the last 3 companies from the list
last_three= it_companies[-3:]
print("last_three: ", last_three)

#Slice out the middle IT company or companies from the list

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
#Remove the middle IT company or companies from the list

#Remove the last IT company from the list
it_companies.pop(len(it_companies)-1)
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies

"""
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
back_end.extend(front_end)
print(back_end)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=back_end.copy()
full_stack.append("python")
full_stack.append("SQL")
print(full_stack)








