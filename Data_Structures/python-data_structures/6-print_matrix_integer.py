"""
Write a function that prints a matrix of integers.


Prototype: def print_matrix_integer(matrix=[[]]):



Format: see example

You are not allowed to import any module

You can assume that the list only contains integers

You are not allowed to cast integers into strings

You have to use str.format() to print integers


"""
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range (len(row)):
            if col==len(row)-1:
                print("{}".format(row[col]), end="")
            else:
                print("{} ".format(row[col]), end="")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print_matrix_integer(matrix)