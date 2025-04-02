#create a new file
new_file = open("lesson 45/sample1.txt", 'x')
new_file.close()

#check if a file exists
import os
print("=== Checking if my_file exists or not===""")
if os.path.exists("lesson 45/my_file.txt"):
    os.remove("lesson 45/my_life.txt")
else:
    print("The file does not exist")

#create a new if it doesn't exists
my_file = open("lesson 45/sample2.txt", 'w')
my_file.write("Hi! I am Malak from Morocco.")
my_file.close()

#delete file name sample3 if it exists
if os.path.exists("lesson 45/sample3.txt"):
    os.remove("lesson 45/sample3.txt")

#delete the folder if it exists
if os.path.exists("Folder"):
    os.rmdir("Folder")