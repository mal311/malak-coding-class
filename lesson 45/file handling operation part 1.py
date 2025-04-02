#write in file using with() function
with open("lesson 45/sample.txt", 'w') as file:
    file.write("Hi! I am Malak and I'm from Morocco.")
file.close()

#split file into words
with open("lesson 45/sample.txt", 'r') as file:
    data = file.readlines()

    print("Words in this file are:")

    for line in data:
        word = line.split()
        print(word)

file.close()