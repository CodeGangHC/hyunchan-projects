from tkinter import *
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image

root = Tk()
root.title("Gang's GUI")
root.geometry("640x480+800+500") # width * height + x-axis + y-axis

# train ticket booking system
def info():
    msgbox.showinfo("Alert", "Booking completed!")

def warn():
    msgbox.showwarning("Warning", "Selected seat has been sold out!")

def error():
    msgbox.askokcancel("Error", "Error while processing payment")

def okcancel():
    msgbox.askokcancel("Confirm / Cancel", "Selected seat accompanies infant seat, do you still want to proceed?")

def retrycancel():
    msgbox.askretrycancel("Retry / Cancel", "Error, try again?")

def yesno():
    msgbox.askyesno("Yes / No", "Selected seat is reversed seat, do you still want to proceed?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Booking process hasn't been saved.\nWould you like to save before close?")
    # Yes : store then close
    # No : close without storing
    # Cancel: cancel closing programming
    print("Answer: ", response) # True, False, None
    if response == 1: # yes
        print("Yes")
    elif response == 0: # no
        print("No")
    else:
        print("cancel")

Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()
Button(root, command=okcancel, text="Confirm Cancel").pack()
Button(root, command=retrycancel, text="Retry Cancel").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()




def create_new_file():
    pass

root.mainloop()