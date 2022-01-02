import pandas as pd
import numpy as np
import math
import os
from helper_func import importdata_



def clean(data):
    data = data[0].split(',')
    data = [int(i) for i in data]
    arr_data =np.array(data).reshape(1,-1)
    return arr_data

def check_end(arr):
    sum_ =np.where(arr==0,1,0).sum()
    return sum_

def add_arr(arr, add):
    assert arr.shape[0] == add.shape[0]
    return (np.concatenate((arr, add), axis = 1))

def reset_( arr):
    idx = np.argwhere(arr ==0)[:,1].reshape(1,-1)
    arr[0][tuple(list(idx))] += 6
    return arr


def concat_(arr, days):
    curr_arr = arr
    
    for day in range(days):

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
    
    arr_data = clean(data)
    
    amount_lanternfish = concat_(arr_data, 80)
    print(amount_lanternfish)