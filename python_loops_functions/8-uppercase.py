"""
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
"""
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i=chr(ord(i)-32)
        print(f"{i}",end="")
    print()
mystr="nEw"
uppercase(mystr)