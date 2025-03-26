#open file and store file object in a variable
file = open("lesson 43/sample1.txt") #file path from the root of the coding folder

#read the file
print(file.read())

print()

#close the file
file.close()