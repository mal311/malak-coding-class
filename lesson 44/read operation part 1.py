#open file and read its contents
file = open("lesson 44/sample.txt" , "r")
print(file.read())
print()

file.close()

#open file and read its beginning 8 characters
file = open("lesson 44/sample.txt", "r")

print("Read in parts")
print(file.read(8))
file.close()

