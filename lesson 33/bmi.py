height = float(input("enter your height in m = "))
weight = int(input("enter your weight in kg = "))

#calculate the bmi
bmi = weight/(height*height)

print("your bmi is ",bmi)

if bmi <= 18.4:
    print("you are underweight, eat more!")
elif 18.4 < bmi and bmi <= 24.9:
    print("you are healthy!")
elif 24.9 < bmi and bmi <= 29.9:
    print("you are overweight, eat less!")
elif 29.9< bmi and bmi <= 34.9:
    print("you are severely overweight!")
else:
    print("you are obese, go see the doctor!!")