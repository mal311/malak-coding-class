class Addition :
    #define a constructor
    def __init__(self,x,y,z):
        self.num1 = x
        self.num2 = y
        self.num3 = z

    def result(self):
        self.result = self.num1 + self.num2 + self.num3
        print("Total:", self.result)

#object which calls the constructor
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

sum = Addition(x,y,z)
sum.result()