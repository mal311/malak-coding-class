number = 1
sum = 0

#calculating using while loops
while number<= 10 :
    sum = sum + number
    number = number + 1

print(f"sum of first 10 natural numbers using while loops = {sum}")
print()

#reseting variables value
number = 1
sum = 0

#calculating using for loops
for i in range(number, 11):
    sum = sum+ i

print(f"sum of first 10 natural numbers using for loops = {sum}")