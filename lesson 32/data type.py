name = "malak"
age = 15
height = 1.6

print("name = ",name)
print("data type of name is ",type(name))
print()

print("age = ",age)
print("data type of age is ",type(age))
print()

print("height = ",height)
print("data type of height is ",type(height))
print()

#type casting or change the data type
print("original age= ",age)
print("original data type of age = ",type(age))
print()

#change data type of age
age = float(age) #change from integer to float
print("age after type casting = ",age)
print("data type of age after type casting = ",type(age))