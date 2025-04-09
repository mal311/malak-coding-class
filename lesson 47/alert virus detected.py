from tkinter import *
from tkinter import messagebox

#setup tkinter window
window = Tk()
window.title('Messagebox')
window.geometry('200x200')

#function for displaying warning message
def msg():
    messagebox.showwarning("Alert", "Stop!virus found")

#Adding button widget to window
button = Button(window, text="Scan for virus", fg="blue", bg="yellow", command=msg)
button.place(x=50, y=80)

#Entering main event loop
window.mainloop()