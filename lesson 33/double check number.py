number = int(input("enter number to be checked = "))

if number > 50:
    print("this number is greater than 50")

    if number%2 == 0:
        print("and it is even number as well")
    else:
        print("and it is odd number as well")
else:
    print("this number is less than or equals to 50")
