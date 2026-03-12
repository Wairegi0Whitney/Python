"""
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals
"""
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str=f"{str[38:67]+str[106:112] +str[:6]}"
print(str)

