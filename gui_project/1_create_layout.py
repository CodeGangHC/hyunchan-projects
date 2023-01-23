import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Gang's GUI")

# file frame (add file, delete file)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete")
btn_del_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Saving location frame
path_frame = LabelFrame(root, text="Store Path")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="Search", width=10)
btn_dest_path.pack(side="right")

# option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack()

# 1. width option
# width label
lbl_width = Label(frame_option, text="width", width=8)
lbl_width.pack(side="left")

# width combo
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

# 2. space option
# space label

# space combo

# 3. file format option



root.resizable(False, False) # unable to resize
root.mainloop()