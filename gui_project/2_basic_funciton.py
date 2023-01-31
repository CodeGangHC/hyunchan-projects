import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog # has to import submodule

root = Tk()
root.title("Gang's GUI")

# file frame (add file, delete file)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# add file
def add_file():
    files = filedialog.askopenfilenames(title="Select Image File", \
        filetypes=(("PNG File", ".png"), ("All Files", "*.*")), \
        initialdir=r"C:\Users\Gang\Desktop") # open at the desktop

    # list of files that User has selected
    for file in files:
        list_file.insert(END, file)

# delete file (folder)
def delete_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# store location
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# start
def start():
    # check options
    print("width: ", cmb_width.get())
    print("space: ", cmb_space.get())
    print("format: ", cmb_format.get())

    # check file list
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add image files")
        return

    # check store location
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select store location")
        return


btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete", command=delete_file)
btn_del_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Store location frame
path_frame = LabelFrame(root, text="Store Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Search", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. width option
# width label
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# width combo
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. space option
# space label
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# space combo
opt_space = ["None", "Narrow", "Medium", "Wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. file format option
# file format label
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# file format combo
opt_format = ["PNG", "JPB", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Prgoress frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False) # unable to resize
root.mainloop()