from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Entry box")
root.geometry("500x500")

# Create Entry Function
def speak():
    my_label.config(text= f"You have typed {my_entry.get()}")
# Create Entry Widget
my_entry = tb.Entry(root, bootstyle="success", font = ("Helvetica", 18), foreground="green")
my_entry.pack(pady = 20)

# Create Button
my_button = tb.Button(root, bootstyle="danger, outline", text="Click Me", command= speak)
my_button.pack(pady = 20)

# Create Label
my_label = tb.Label(root, text = "")
my_label.pack(pady = 20)

# Create Entry Widget for password
my_entry2 = tb.Entry(root, bootstyle="success", font = ("Helvetica", 18), foreground="green", show="*")
my_entry2.pack(pady = 20)

root.mainloop()