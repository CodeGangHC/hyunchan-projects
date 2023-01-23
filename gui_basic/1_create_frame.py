from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")
btn5.pack()

photo = ImageTk.PhotoImage(Image.open('img.png'))
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button has been pressed")

btn7 = Button(root, text="Working Button", command=btncmd)
btn7.pack()

# root.geometry("640x480+800+500") # width * height + x-axis + y-axis
#
# root.resizable(False, False) # not allowing switching x-axis and y-axis size (unable to resize window size)

root.mainloop()