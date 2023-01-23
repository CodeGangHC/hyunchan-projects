from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Insert txt")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Insert only one line")

def btncmd():
    # print contents
    print(txt.get("1.0", END)) # 1: first line, 0: 0th column
    print(e.get())

    # remove contents
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()