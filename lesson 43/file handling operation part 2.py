#open the file in read mode
file_read = open("lesson 43/sample2.txt", "r")
print("File in Read Mode - ")
print(file_read.read())
file_read.close()

print()

#open the file in write mode to replace te original content with new sentence
file_write = open("lesson 43/sample2.txt", "w")

#write in the file
file_write.write("file in write mode...")
file_write.write("\nI am hungry")
file_write.close()

#open the file in append mode to combine original sentence with new sentence
file_append = open("lesson 43/sample2.txt", "a")

#append the file
file_append.write("\nFile in append mode...")
file_append.write("\n Today is a fine day")
file_append.close()