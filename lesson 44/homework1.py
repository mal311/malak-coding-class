#read first 2 lines of file
file = open("lesson 44/homework.txt", "r")
print("===Reading first 2 line===")
print(file.readline())
print(file.readline())
file.close()

print()


#read first line of file
file = open("lesson 44/homework.txt", "r")
print("===Reading first line===")
print(file.readline())
file.close()

print()