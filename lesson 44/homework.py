
file = open("lesson 44/homework.txt" , "r")
print(file.read())
print()

file.close()



file = open("lesson 44/homework.txt", "r")

print("Read in parts")
print(file.read(8))
file.close()
print()


file = open("lesson 44/homework.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())

file.close()

print()
