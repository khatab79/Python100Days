from tkinter import *

window = Tk()

window.title("GUI Test")

window.minsize(width=500, height=300)

mylabel = Label(text="test label",font=(55))
mylabel.pack()

def click():
    mylabel.config(text=input.get())
    print()

button = Button(text="click me",command=click)
button.pack()

input = Entry()
input.pack()



window.mainloop()