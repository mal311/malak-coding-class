from tkinter import *
from PIL import Image, ImageTk

#create a window with a title bar and set its geometry as well
window = Tk()
window.title('image')
window.geometry('400x400')

#Now use image.open to open and identifythe given image file
upload = Image.open("lesson 47/space.jpg")

#convert this image to tkinter compatible image
image2=ImageTk.PhotoImage(upload)

#add image to tkinter label
label = Label(window, image=image2, height=250, width=300)
label.place(x=50, y=20)

label2 = Label(window, text="space")
label2.place(x=150, y=290)

#run the application
window.mainloop()