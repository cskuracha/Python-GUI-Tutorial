from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename= "superhero")
root.title("TTK Bootstrap !!")
root.geometry('500x500')

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked !")
    else:
        my_label.config(text = "Unchecked !!")

my_label = tb.Label(text = "Click the checkbutton below", font = ("Helvetica", 18), bootstyle = "default")
my_label.pack(pady = (40,20))

#Checkbutton
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle= "info", text = "Check me out!", variable = var1, onvalue = 1, offvalue=0, command= checker)
my_check.pack(pady = 10)

#Toolbutton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle = "primary, toolbutton", text = "Tool Button", variable = var2, onvalue= 1, offvalue = 0, command = checker)
my_check2.pack(pady = 10)

# Outlined Toolbutton
var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle = "primary, toolbutton, outline", text = "Outline Tool Button", variable = var3, onvalue= 1, offvalue = 0, command = checker)
my_check3.pack(pady = 10)

# Round Toggle Button
var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle = "success, round-toggle", text = "Round Toggle Button", variable = var4, onvalue= 1, offvalue = 0, command = checker)
my_check4.pack(pady = 10)

# Square Toggle Button
var5 = IntVar()
my_check5 = tb.Checkbutton(bootstyle = "warning, square-toggle", text = "Square Toggle Button", variable = var5, onvalue= 1, offvalue = 0, command = checker)
my_check5.pack(pady = 10)
root.mainloop()