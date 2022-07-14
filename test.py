from PIL import ImageGrab
from time import sleep
import numpy as np
from PIL import Image
import sys
import win32gui



# win = win32gui.FindWindow(None,"Minecraft")
# rect = win32gui.GetWindowRect(win)
# print(rect)
# sleep(5)
# center_x,center_y = [(rect[2]-rect[0])/2+rect[0],(rect[3]-rect[1])/2+rect[1]]
# cap_size =100
# print(center_x,center_y)
# capture = ImageGrab.grab(bbox=(center_x-cap_size, center_y-cap_size, center_x + cap_size, center_y + cap_size))
# # capture = ImageGrab.grab(bbox=rect)

# capture.save("./cap.png")
# capture = Image.open("floater_at_night.png")
# cap = np.array(capture)
# np.set_printoptions(threshold=sys.maxsize)
# mask_r = (cap[:,:,0]>50)&( cap[:,:,1]<100 )&( cap [:,:,2]<100)
# print(cap[:,:,0])
# print(mask_r.sum())
# cap_new=cap.copy()
# cap_new[:,:,0] = cap[:,:,0]*mask_r
# cap_new[:,:,1] = cap[:,:,1]*mask_r
# cap_new[:,:,2] = cap[:,:,2]*mask_r

# nimage=Image.fromarray(cap_new)
# nimage.show()

capture = Image.open("floater_at_night_only.png")
np.set_printoptions(threshold=sys.maxsize)
capture.convert("HSV")
capture[:,:,2]
cap = np.array(capture)
print(cap[0:10,:,:])