from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("TTk Bootstrap")
root.geometry('500x500')

# Adding a Label
my_label = tb.Label(text = "Hello World!", font= ("Helvetica", 28), bootstyle = "default")
my_label.pack(pady = 50)



root.mainloop()

