#recursive function
def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1) #sending a value after calling the function itself
    
num = int(input("enter a number = "))



if num < 0:
    print("factorial does not exist for negative number")
elif num == 0:
    print("the factorial of 0 is one")
else:
    result = factorial(num)
    print(f"the factorial of {num} is {result}")