class cat: #cat constructor
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I'm a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class dog: #dog constructor
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I'm a dog. My name is {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Woof Woof")

cat1 = cat("kitten", 2.5)
dog1 = dog("Frenzy", 3)

for animal in (cat1, dog1): #representing cat1 and dog1 as animals
    animal.make_sound()
    animal.info()
    print()