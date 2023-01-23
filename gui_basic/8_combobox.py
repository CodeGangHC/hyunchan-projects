from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

values = ["date: " + str(i) for i in range(1, 32)] # 1 ~ 31
combobox = ttk.Combobox(root, height=5, width=30, values=values, state="readonly")
combobox.pack()
combobox.current(0)
def btncmd():
    print(combobox.get())

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()