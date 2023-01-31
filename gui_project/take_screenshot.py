import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2023 January 31 09:10:15 -> 20230131_091015
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20230131_091015.png

keyboard.add_hotkey("ctrl+shift+s", screenshot) # press ctrl + shift + s to take a screenshot

keyboard.wait("esc") # run program until user presses ESC
