from tkinter import *
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry("640x480+900+500")

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # if file exist = True, else = False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # delete main text widget before open file
            txt.insert(END, file.read())

def save_new_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # store all the contents

menu = Menu(root)

# creating file menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_new_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# edit, format, view, help menu
menu.add_cascade(label="Edit")
menu.add_cascade(label="Formant")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# main text area
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()