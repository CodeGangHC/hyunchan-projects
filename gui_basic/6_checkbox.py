from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

chkvar = IntVar() # store value as int into the chkvar
chkbox = Checkbutton(root, text="Skip it for today", variable=chkvar)
chkbox.select()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Skip for a week", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: unchecked, 1: checked
    print(chkvar2.get())



btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()