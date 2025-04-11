from tkinter import *

window = Tk()
window.title('ROCK PAPER SCISOR')
window.geometry('200x200')

label= Label(window, text="rock paper scissors game")
label.place(x=150, y=290)

#Adding button widget to window
button = Button(window, text="rock", fg="white", bg="blue")
button.place(x=10, y=80)

button = Button(window, text="paper", fg="white", bg="blue")
button.place(x=70, y=80)

button = Button(window, text="scissor", fg="white", bg="blue")
button.place(x=130, y=80)


#Entering main event loop
window.mainloop()