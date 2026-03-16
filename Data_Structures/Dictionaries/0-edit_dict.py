MyDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(MyDict)
print(MyDict["model"])

#get specific items from a dictionary
x=MyDict.get("model")
print(x)

#get the keys in the dictionary

y=MyDict.keys()
print(y)