from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# without set, scroll won't move
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32): # 1~31
    listbox.insert(END, "date: " + str(i))
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # scrollbar gets attached to the screen and moves along

root.mainloop()