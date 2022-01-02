import pandas as pd
import numpy as np
import math
import os
from helper_func import importdata_
from collections import Counter


def count(data):
    print(list(Counter(data).values()))
    return Counter(data)

    
    
def clean(data):
    data = data[0].split(',')
    data = [int(i) for i in data]
    counts =count(data)
    counted = [counts[i] for i in range(7)]
    set_data = np.array((list(set(data)))).reshape(1,-1)
    arr_data =np.longdouble(data).reshape(1,-1)
    return arr_data, counted, set_data

def check_end(arr):
    sum_ =np.where(arr==-1,1,0).sum()
    return sum_

def add_arr(arr, add):
    assert arr.shape[0] == add.shape[0]
    return (np.concatenate((arr, add), axis = 1))

def reset_( arr):
    idx = np.argwhere(arr ==-1)[:,1].reshape(1,-1)
    arr[0][tuple(list(idx))] += 7
    return arr


def concat_(arr, days, print_ = False):
    curr_arr = arr
    
    for day in range(1, days+1):
        if print_:
            print(f"Day: {day}/{days}, Amount: {curr_arr.shape[1]}")

        sub = np.ones(curr_arr.shape)
        curr_arr= curr_arr - sub
        
        #check how much we need to add
        to_add = check_end(curr_arr)
        add_to_arr = np.zeros([1,to_add]) + 8
        
        curr_arr = add_arr(curr_arr, add_to_arr)
        curr_arr = reset_(curr_arr)

    # when concat: add the sum of init values with 6 to the end of the array. 
    return curr_arr.shape[1]
    
    


if __name__ == "__main__":
    path= 'Data_sets/‏‏data_6.txt'
    data  = importdata_(path, 'r')
    
    arr_data,counted, set_array = clean(data)
    
    amount_lanternfish = concat_(arr_data, 80, print_ = True)
    print()
    amount_lanternfish2 = concat_(set_array, 256, print_ = True)

    print(amount_lanternfish)