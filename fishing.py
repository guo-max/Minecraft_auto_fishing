import pyautogui
from PIL import ImageGrab
from time import sleep
import numpy as np
import win32gui

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True
    # moving the mouse to the upper-left
    # corner will abort your program. This prevents 
    # locking the program up.
    pyautogui.FAILSAFE = True

def take_capture(center,cap_size):
    center_x,center_y = center  
    capture = ImageGrab.grab(bbox=(center_x-cap_size, center_y-cap_size, center_x + cap_size, center_y + cap_size))
    return np.array(capture)
def find_red_stripe(capture):
    red_stripe_mask = (capture[:,:,0] > 100) & (capture[:,:,1] < 80) & (capture[:,:,2] < 80)
    return red_stripe_mask.sum()

def auto_fishing(center ,cap_size,threshold):

    pyautogui.rightClick()  # cast the fishing line
    sleep(2)
    # baseline should find the floater
    baseline=find_red_stripe(take_capture(center,cap_size))
    print("baseline of redness: "+str(baseline))
    if(baseline < threshold):
        print("can not find the floater.")
        pyautogui.rightClick()  # cast the fishing line
        sleep(2)
        return 

    current_redness= find_red_stripe(take_capture(center,cap_size))
    print("current redness: "+str(current_redness))
    counter = 0
    while(baseline-current_redness<threshold and counter <100):
    
        sleep(0.2)
        counter = counter+1
        current_redness= find_red_stripe(take_capture(center,cap_size))
        print("current redness: "+str(current_redness))
    pyautogui.rightClick()
    if (counter==100):
        print("no fish")
    else:
        print("got a fish!")
    sleep(1)

def main():
    initializePyAutoGUI()
    win = win32gui.FindWindow(None,"Minecraft")
    rect = win32gui.GetWindowRect(win)
    center = [(rect[2]-rect[0])/2+rect[0],(rect[3]-rect[1])/2+rect[1]]
    sleep(5)  
    i = 0
    while i < 100:
        auto_fishing(center,100,15)
        i += 1
if __name__ == "__main__":
    main()