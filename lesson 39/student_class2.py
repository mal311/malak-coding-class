class student:
    grade = 10
    name = "Malak"

    def introduction(self) : #method1
        print("Hi I am a student")

    def details(self) : #method2
        print("my name is ", self.name)
        print("I study in grade", self.grade)

ob = student() #create new object
ob.introduction()
ob.details()
