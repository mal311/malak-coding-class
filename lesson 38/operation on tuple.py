my_tuple = () #empty tuple
print(my_tuple)
print()

#Tuple having integers
my_tuple = (1, 2, 3)
print("tuple with integer values :", my_tuple)

#Tuplewith mixed data types
my_tuple = (1, "hello", 3,4)#integer, string, float
print("tuple with mixed data types :", my_tuple)

#nested tuple
my_tuple = ("mouse", [8, 4, 6], (3, 5, 6))#string, list, another tuple
print("nested tuple :", my_tuple)
print()

#nested tuple
n_tuple = ("mouse", [8, 4, 6], (3, 5, 6))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])
print()

#Accessing tuple element using indexing
my_tuple =('b', 'e', 'a', 'u', 't', 'y')
print(my_tuple[0])
print(my_tuple[5])
print()


#Iterating trough tuple
for letter in (my_tuple):
    print("Hello", letter)#iterating means repetition
