import urllib.request, json 
import requests
import numpy as np
import os


print (os.getcwd())


with open ('C:/Users/admin/Documents/GitHub/Avent_Of_Code_Challenge_2021/data_2.txt', 'r') as data_day_2:
    data = data_day_2.readlines()
    
    
def movement(data):
    """
    up: decreases your depth
    down: add to depth
    forward: add horizintal
    (h,d)
    """
    loc =np.zeros(2)
    for idx, (itter) in enumerate((data)):
        itter= (itter.split(' '))
        step, val = (str(itter[0])[0]).lower(), int(itter[-1])
        if (step =='u'):
            move = np.array((0,-val))
        elif (step =='d'):
            move = np.array((0,val))
        elif step =='f':
            move = np.array((val,0))

        loc  +=move

        if idx ==len(data)-1:
            return loc[0] * loc[1]
        
def movement_2(data):
    """
    down X increases your aim by X units ---
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

    (h,d,a)
    """
    loc =np.zeros(3)
    for idx, (itter) in enumerate((data)):
        itter= (itter.split(' '))
        step, val = (str(itter[0])[0]).lower(), int(itter[-1])
        if (step =='u'):
            move = np.array((0,0,-val))
        elif (step =='d'):
            move = np.array((0,0,val))
        elif step =='f':
            depth = loc[2] * val
            move = np.array((val,depth, 0))

        loc  +=move

        if idx ==len(data)-1:
            return loc[0] * loc[1]
        
        
print(movement_2(data))
