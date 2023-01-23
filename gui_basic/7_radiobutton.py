from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

Label(root, text="Select Menu").pack()

burger_var = IntVar() # store value as int
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select() # default burger
btn_burger2 = Radiobutton(root, text="Chicken Hamburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Cheese Hamburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Select yoru drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select() # default drink
btn_drink2 = Radiobutton(root, text="Sprite", value="Sprite", variable=drink_var)
btn_drink3 = Radiobutton(root, text="Dr.Pepper", value="Dr.Pepper", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # return selected value from the burger radiobutton
    print(drink_var.get())

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()