#!/usr/bin/env python3

"""
key codes:
    events:
    n = head nodding
    b = head bobbing
    v = vocalization
    w = whisteling
    m = moving
    h = head whips
    
    behaviors:
    p = pruning
    s = stretching
    e = eating
    l = standing on one leg
    i = nibbling
    f = feathers puffing
"""
#RUN CODE WHEN VIDEO STARTS. STOPWATCH WILL START WHEN CODE RUNS

from pynput import keyboard
from stopwatch import Stopwatch

stopwatch = Stopwatch()

def get_key_name(key):
        if isinstance(key, keyboard.KeyCode):
            return key.char
        else:
            return str(key)

#PRESS SHIFT TO PAUSE TIMER
#PRESS SPACEBAR WHEN VIDEO STARTS TO START TIMER AGAIN
#PRESS CORRESPONDING KEY WHENEVER ACTIVITY STARTS/STOPS
def on_press(key):
    key_name = get_key_name(key)
    if key_name == "Key.shift":
        stopwatch.stop()
    elif key_name == "Key.space":
         stopwatch.start()
    else:
        print('{}'.format(key_name), stopwatch.duration)

#END PROGRAM WHEN VIDEO ENDS BY PRESSING ESC     
def on_release(key):
    key_name = get_key_name(key)     
    if key_name == 'Key.esc':
        print("end")
        return False
    
with keyboard.Listener(on_press = on_press, 
                       on_release = on_release) as listener:
    listener.join()
    
    
#COPY AND PASTE RESULTS INTO PLAINTEXT FILE AND SAVE WITH VIDEO NUMBER: "day[day#].[session#].[video#].txt" 
    #example: day2.1.4.txt
    