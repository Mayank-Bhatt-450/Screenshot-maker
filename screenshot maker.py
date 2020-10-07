import PIL.ImageGrab
import os
def ss():
    im = PIL.ImageGrab.grab()
    f=os.listdir('.')
    k=0
    while True:
        
        g=str(k)+'.jpg'
        if  g in f:
           k+=1
        else:
            print(g)
            im.save(g)
            break
from pynput import keyboard
import pyautogui
import time
def on_press(key):
    #print(str(key))
    if str(key) == 'Key.print_screen':
        ss()

with keyboard.Listener(
    on_press = on_press,) as listener:
    listener.join()
