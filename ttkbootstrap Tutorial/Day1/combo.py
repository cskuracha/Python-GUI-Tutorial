from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename = "superhero")
root.title("TTK Bootstrap ! Combobox")
root.geometry("500x500")

# Creating button click function
def clicker():
    my_label.config(text= f"You have selected {my_combo.get()}")

# Creating binding function
def click_bind(e):
    my_label.config(text=f"You have selected {my_combo.get()}")

my_label = tb.Label(text="Hello World!", font=("Helvetica", 18))
my_label.pack(pady = 20)

# Creating Dropdown options
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#create combo box
my_combo = tb.Combobox(root, bootstyle="success", values = days)
my_combo.pack(pady = 20)

#Set Combo default
my_combo.current(0)

# Create Button
my_button = tb.Button(root, text = "Click Me!", command = clicker, bootstyle= "danger")
my_button.pack(pady = 10)

# Bind the combo box
my_combo.bind("<<ComboboxSelected>>",click_bind)

root.mainloop()