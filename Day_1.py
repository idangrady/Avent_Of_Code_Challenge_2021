import urllib.request, json 
import requests
import numpy as np


def open_file(filename, operation):
    with open(filename, operation) as file_1:
        return file_1.readlines()

def how_often_increase(data):
    count = 0
    for previous_loc, loc in enumerate(range(1,len(data))): 
        
        current = data[loc]
        previous = data[previous_loc]

        if current > previous: 
            count +=1

    return count
            
            

def three_consec(data):
    data = list(map(int,data))
    count = sum(
        ((np.sum(data[i + 1 : i + 4])) > (np.sum(data[i : i + 3])))
        for i in range(len(data))
    )

    print(count)
                    
        






# =============================================================================
# 
# path = r'data_2.txt'
# operation = 'r'
# data =open_file(path, operation)
# 
# print(len(data))
# print(how_often_increase(data))
# 
# three_consec(data)
# =============================================================================
