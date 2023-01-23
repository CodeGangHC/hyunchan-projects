import time
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # moves every 10 ms
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
# btn = Button(root, text="Pause", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # range of 1 ~ 100
        time.sleep(0.01) # hold for 0.01 sec

        p_var2.set(i) # set the value of progress bar
        progressbar2.update() # ui update
        print(p_var2.get())

btn = Button(root, text="Start", command=btncmd2)
btn.pack()

root.mainloop()