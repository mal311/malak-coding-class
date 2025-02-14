attendance = int(input("enter your total attendance days "))
absent = int(input("enter your total absent days "))

pourcentage = ((attendance - absent)/attendance)*100

if pourcentage >= 75:
    print("you are eligible for exam")
else:
    print("you are not eligible for exam")