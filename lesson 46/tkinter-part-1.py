from tkinter import *

#creating window
window = Tk()
window.title("Tkintle sample window")
window.geometry("400x300")#width = 400 , height = 300

#Label 
greeting = Label(text="Hello I am label", fg="black", bg="pink")

#button
button = Button(text="Click me, I am a button", bg="blue", fg="white")

#entry
entry = Entry(fg="white", bg="green", width=30)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="Sample Frame")
label.pack()

textbox = Text(bg="yellow", fg="purple")
textbox.pack()

window.mainloop()