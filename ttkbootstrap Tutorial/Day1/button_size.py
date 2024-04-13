from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("TTK Bootstrap")
root.geometry("500x500")

#Configuring Style
my_style = tb.Style()
my_style.configure('success.TButton', font =("Helvetica", 18))


my_button = tb.Button(text="Hello World", bootstyle= "success", style= "success.TButton")
my_button.pack(pady = 10)

# success Outline
my_style2 = tb.Style()
my_style2.configure('success.Outline.TButton', font =("Helvetica", 18))


my_button2 = tb.Button(text="Hello World", bootstyle= "success", style= "success.Outline.TButton", width = 20)
my_button2.pack(pady = 10)

root.mainloop()