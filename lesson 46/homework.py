import random
#print a message to let the user know the program has strated
print("starting password generator...")

#define the set of characters that can be used in the password
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?"

#get the desied length of the password from the user input
password_length = int(input("Enter desired password length: "))

#initialize an empty list to store password characters
password = []

#loop through a range of numbers from 0 to the desired password lengh
for i in range(password_length):
    password.append(random.choice(characters))


#join all characters in the list into a single string
pwd = ''.join(password)

#output the generayed password
print("Your new password is:" +pwd)