from msilib.schema import Font
from tkinter import *

PADDING = 5
FONT= ("Arial", 24 ,"bold")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30,pady=30)
# window.minsize(width=300, height=200)

def onclick():
    mile = int(input.get())
    km = round(1.60934 * mile)
    lbl_result.config(text=km)

# labels
lbl_mile = Label(text="Miles")
lbl_mile.grid(column=2, row=0)
lbl_mile.config(padx=PADDING,pady=PADDING)

lbl_km = Label(text="Km")
lbl_km.grid(column=2, row=1)
lbl_km.config(padx=PADDING,pady=PADDING)

lbl_equal = Label(text="is equal to")
lbl_equal.grid(column=0, row=1)
lbl_equal.config(padx=PADDING,pady=PADDING)

lbl_result = Label(text="0")
lbl_result.grid(column=1, row=1)
lbl_result.config(padx=PADDING,pady=PADDING)

# Entry
input = Entry()
# input.insert(END, string="0")
input.config(width=7)
input.grid(column=1, row=0)

# button
btm_calculate = Button(text="Calculate", command=onclick)
btm_calculate.grid(column=1, row=2)
btm_calculate.config(padx=PADDING,pady=PADDING)



window.mainloop()