"""
Write a function that returns a tuple with the length of a string and its first character.


Prototype: def multiple_returns(sentence):



If the sentence is empty, the first character should be equal to None

You are not allowed to import any module

"""
def multiple_returns(sentence):
    if len(sentence)==0:
        tuple_a=(len(sentence),None)
    else:
        tuple_a=(len(sentence),sentence[0])
    print(tuple_a)

profile=""
multiple_returns(profile)