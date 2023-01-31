import time
from PIL import ImageGrab

time.sleep(5) # pause for 5 sec : while user gets ready

for i in range(1, 11): # total 10 images every 2 sec
    img = ImageGrab.grab() # store current screen image into img
    img.save("image{}.png".format(i)) # save into a file by (image1.png ~ image10.png)
    time.sleep(2) # every 2 sec
