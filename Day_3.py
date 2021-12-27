
import numpy as np
import os
from Day_1 import open_file

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def make_array_int(data):
    lists = []
    for arr in data:
        arr_ele = ([int(x) for x in arr.strip() ])#.reshape(1,-1)
        lists.append(arr_ele)
    return np.array(lists)
    

def part_1(data):   
    array_data = make_array_int(data)
    average__ = np.average(array_data, axis = 0)
    eps_ = list( np.where(average__>= 0.5,1,0))
    gamma_ = np.where(average__<= 0.5,1,0)

    return (int(binatodeci(eps_))) * (int(binatodeci(gamma_)))


def part_2(data):
    array_ = make_array_int(data)
    d,n = array_.shape

    remine_ox = array_
    remine_co2 = array_


    output_oxygen =[]
    output_co2 =[]
    for i in range(n):
        average__ox  = np.average(remine_ox[:,i], axis = 0)
        average__co2  = np.average(remine_co2[:,i], axis = 0)

        decide_oxygen  =np.where(average__ox>=0.5,1,0)
        decide_co2  =np.where(average__co2>=0.5,0,1)

        output_oxygen.append(decide_oxygen)
        output_co2.append(decide_oxygen)


        d_ox, n_ox = remine_ox.shape
        d_co, n_ox = remine_co2.shape

        if d_co == 1:
            pass
        elif d_ox == 1:
            remine_co2 = remine_co2[remine_co2[:,i]==decide_co2]
        else: 
            remine_ox = remine_ox[remine_ox[:,i]==decide_oxygen]
            remine_co2 = remine_co2[remine_co2[:,i]==decide_co2]

    num_ox = binatodeci(remine_ox[0])
    num_co = binatodeci(remine_co2[0])
    return(num_ox * num_co)
    #return ( (int(binatodeci(list(remine_ox)))) * (int(binatodeci(list(remine_co2)))))


path ='C:/Users/admin/Documents/GitHub/Avent_Of_Code_Challenge_2021/Data_sets/data_3.txt'
data = open_file(path, 'r')

print(part_1(data))
print(part_2(data))

