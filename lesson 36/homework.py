import turtle

#creating paper or canvas
turtle.Screen().bgcolor("pink")
paper = turtle.Screen()
paper.setup(400, 300) #paper size width=400 height=300

turtle.title("hexagone image")

#creating the pen
pen = turtle.Turtle()

#making a hexagone
pen.pendown()

for i in range(6):
    pen.forward(100) #100 is the size of each side
    pen.left(60)


pen.penup()
pen.right(90)
pen.forward(50) 
turtle.done()