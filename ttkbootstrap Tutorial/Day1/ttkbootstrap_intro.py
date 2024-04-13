from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("TTk Bootstrap")
root.geometry('500x500')

counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text = "Hello World!")
    else:
        my_label.config(text = "Goodbye World!")

# Adding a Label
my_label = tb.Label(text = "Hello World!", font= ("Helvetica", 28), bootstyle = "default")
my_label.pack(pady = 50)

# Adding a Button
my_button = tb.Button(text = "Click Me!", bootstyle = "success, outline", command = changer)
my_button.pack(pady = 30)

root.mainloop()

