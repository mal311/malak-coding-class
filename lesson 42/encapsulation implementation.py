class computer:

    def __init__(self): #constructor
        self.__maxprice = 900 #meansprivate variable
    
    def sell(self):
        print(f"Selling price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = computer() #create object
c.sell()
print()

print("try to update maxprice directly")
#change the price
c.__maxprice = 750
c.sell()
print()

print("after using method setMaxPrice")
#using setter function
c.setMaxPrice(1000)
c.sell()