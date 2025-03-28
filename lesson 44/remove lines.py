#program to remove lines starting with any prefix

file1 = open("lesson 44/sample.txt", "r")
file2 = open("lesson 44/sample1.txt", "w")

#reading each line from original text file
for line in file1.readlines():
    if not(line.startswith('we')): #reading all the line that do not begin with "we"
        print(line)#printing those lines
        file2.write(line)#storing only those lines that do not beging with "we"


#close and save the files
file2.close()
file1.close()