class shape: #parent class
    def __init__(self, w, l, h):
        self.width = w
        self.length = l
        self.name = h

    def __printdetail(self):
        print("Shape: " + self.name)
        print("Width: ",self.width)
        print("Length: ",self.length)

class rectangle(shape):
    def __init__(self, si, le):
        shape_name = "rectangle"
        super().__init__(si, le, shape_name)

    
    def area(self):
        return self.width *self.length