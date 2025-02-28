dict1 = {}

#dictionnary with integer keys
dict1 ={1:"apple",
        2:"ball"
        }

#dictionnary with mixed keys
dict2 ={"name": "John",
        1:[2, 4, 3]
        }

#dictionnary with string keys
dict3 ={"name": "Jack",
        "age": 26,
        "phone": 1234567}

#getting the data
print(dict3["name"])
print(dict.get("age"))
print()

#remove particular element
dict3.pop("age")
print("updated dictionnary 3 after removing age:")
dict3["age"] = 27
print(dict3)
print()