from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

# top row
btnF16 = Button(root, text="F16", width=5, height=2)
btnF17 = Button(root, text="F17", width=5, height=2)
btnF18 = Button(root, text="F18", width=5, height=2)
btnF19 = Button(root, text="F19", width=5, height=2)

btnF16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnF17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btnF18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btnF19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 2nd row
btnClear = Button(root, text="Clear", width=5, height=2)
btnEqual = Button(root, text="=", width=5, height=2)
btnSlash = Button(root, text="/", width=5, height=2)
btnAsterisk = Button(root, text="*", width=5, height=2)

btnClear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnEqual.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btnSlash.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btnAsterisk.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 3rd row
btnSeven = Button(root, text="7", width=5, height=2)
btnEight = Button(root, text="8", width=5, height=2)
btnNine = Button(root, text="9", width=5, height=2)
btnMinus = Button(root, text="-", width=5, height=2)

btnSeven.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnEight.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btnNine.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btnMinus.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4th row
btnFour = Button(root, text="4", width=5, height=2)
btnFive = Button(root, text="5", width=5, height=2)
btnSix = Button(root, text="6", width=5, height=2)
btnPlus = Button(root, text="+", width=5, height=2)

btnFour.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnFive.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btnSix.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btnPlus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 5th row
btnOne = Button(root, text="1", width=5, height=2)
btnTwo = Button(root, text="2", width=5, height=2)
btnThree = Button(root, text="3", width=5, height=2)
btnEnter = Button(root, text="enter", width=5, height=2)

btnOne.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnTwo.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btnThree.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btnEnter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# last row
btnZero = Button(root, text="0", width=5, height=2)
btnPeriod = Button(root, text=".", width=5, height=2)

btnZero.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btnPeriod.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)



root.mainloop()