#check if a file exists
import os
print("=== Checking if homework exists or not===""")
if os.path.exists("lesson 45/sample1.txt"):
    os.remove("lesson 45/sample1.txt")
    print("the file exists")
else:
    print("The file does not exist")

#create a new if it doesn't exists
my_file = open("lesson 45/sample2.txt", 'w')
my_file.write("I love reading")
my_file.close()


#split file into words
with open("lesson 45/sample2.txt", 'r') as file:
    data = file.readlines()

    print("Words in this file are:")

    for line in data:
        word = line.split()
        print(word)

file.close()