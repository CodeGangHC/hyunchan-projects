from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()

def btncmd():
   # listbox.delete(0) # remove the first content

   print("Selected contents : ", listbox.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()