from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")

label1 = Label(root, text="Hello")
label1.pack()

photo = ImageTk.PhotoImage(Image.open('img.png'))
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See ya again")

    global photo2
    photo2 = ImageTk.PhotoImage(Image.open('img2.png'))
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()