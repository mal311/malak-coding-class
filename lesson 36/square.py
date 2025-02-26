import turtle

#creating paper or canvas
turtle.Screen().bgcolor("blue") #setting the paper color
paper = turtle.Screen()
paper.setup(400, 300) #paper size width=400 height=300

turtle.title("square image")

#creating the pen
pen = turtle.Turtle()

#making a square
pen.pendown()

for i in range(4):
    pen.forward(100) #100 is the size of each side
    pen.left(90) #square angle

pen.penup()
pen.right(90)
pen.forward(50) 
turtle.done()