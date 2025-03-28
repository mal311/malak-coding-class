#read first line of file
file = open("lesson 44/sample.txt", "r")
print("===Reading first line===")
print(file.readline())
file.close()

print()

#read first 2 lines of file
file = open("lesson 44/sample.txt", "r")
print("===Reading first 2 line===")
print(file.readline())
print(file.readline())
file.close()

print()

#looping through all the line of the file
file = open("lesson 44/sample.txt", "r")
print("===Looping through the lines")
for line in file:
    print(line)
    
file.close()