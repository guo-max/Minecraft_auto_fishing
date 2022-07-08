import pyautogui
from PIL import ImageGrab
from time import sleep
import numpy as np

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True
    # moving the mouse to the upper-left
    # corner will abort your program. This prevents 
    # locking the program up.
    pyautogui.FAILSAFE = True

def take_capture(cap_size):
    mouse_x,mouse_y = pyautogui.position()  
    capture = ImageGrab.grab(bbox=(mouse_x-cap_size, mouse_y-cap_size, mouse_x + cap_size, mouse_y + cap_size))
    return np.array(capture)
def find_red_stripe(capture):
    red_stripe_mask = (capture[:,:,0] > 120) & (capture[:,:,1] < 100) & (capture[:,:,2] < 110)
    return red_stripe_mask.sum()

def auto_fishing(cap_size,threshold):

    pyautogui.rightClick()  # cast the fishing line
    sleep(2)
    # baseline should find the floater
    baseline=find_red_stripe(take_capture(cap_size))
    print("baseline of redness"+str(baseline))
    current_redness= find_red_stripe(take_capture(cap_size))
    print("current redness"+str(current_redness))
    counter = 0
    while(baseline-current_redness<threshold and counter <100):
    
        sleep(0.2)
        counter = counter+1
        current_redness= find_red_stripe(take_capture(cap_size))
        print("current redness"+str(current_redness))
    pyautogui.rightClick()
    if (counter==100):
        print("no fish")
    else:
        print("got a fish!")
    sleep(1)

def main():
    initializePyAutoGUI()
    sleep(5)  
    i = 0
    while i < 100:
        auto_fishing(100,30)
        i += 1
if __name__ == "__main__":
    main()