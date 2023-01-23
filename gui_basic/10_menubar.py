from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

def create_new_file():
    print("Creating a new file")

menu = Menu(root)

# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Edit Menu
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Cut")
menu_edit.add_command(label="Copy")
menu_edit.add_command(label="Paste")
menu_edit.add_separator()
menu_edit.add_command(label="Find...")
menu.add_cascade(label="Edit", menu=menu_edit)

# Language Menu (using radio button to select 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View Menu (using check box)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()