class Person: #parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Fullname "+ self.firstname + " " + self.lastname)

class student(Person): #child class
    def __init__(self, fn, ln, year):#student's constructor
      super().__init__(fn, ln)#triggering parent's constructor

      self.graduationyear = year

x = student("Malak", "Imaddahen", 2025)
x.printname()
print("Graduation year:" ,x.graduationyear)