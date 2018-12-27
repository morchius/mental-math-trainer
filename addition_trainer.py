# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:06:19 2018

@author: Claudius
"""

import win32com.client as wincl
import numpy as np
import time
import random

speak = wincl.Dispatch("SAPI.SpVoice")


def draw_operation_and_number():
    rand = np.random.randint(low = 10, high = 100, size = 1)
    operation = random.choice([0,1,1])
    print(operation)
    if operation:
        rand = "plus " + str(rand[0])
    else:
        rand = "minus " + str(rand[0])
    return(rand)

    
def run_training(numb_of_rounds):
    n = 0
    control = "run"
    count = 0
    while (n < numb_of_rounds) and (control == "run"):
        res = draw_operation_and_number()
        speak.Speak(res)
        if res.split()[0] == "minus":
            count = count - int(res.split()[1])
        else:
            count = count + int(res.split()[1])
        key = input("Want to stop? Press 0!\nPress any key to continue!")
        if key == 0:
            control = "stop"
        n += 1
        if (control == "stop") or (n == numb_of_rounds):
            print("Count is: {}".format(count))
    return(count)
            
    