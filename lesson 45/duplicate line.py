#Program to eliminate repeated lines from a file

#creating the output file
outputFile = open("lesson 45/sample5.txt", "w")

#reading the input file
inputFile = open("lesson 45/sample4.txt", "r")

#hold lines already seen
lines_seen_so_far = set()
print("===Eliminating duplicate lines===")

for line in inputFile:
    if line not in lines_seen_so_far: #checking if line is unique
      outputFile.write(line)#write unique lines in output file
      lines_seen_so_far.add(line)#adds uniqu lines to lines_seen_so_far

#closing the file
inputFile.close()
outputFile.close() 