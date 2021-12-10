from Day_1 import open_file
import sys, os
import numpy as np


def split_data(data):
    list_of_objects = []
    current_list = []
    hash_table = []
    for idx, line in enumerate(data):
        if idx==0:
            line = line.replace(',','' )
            list_values = [int(x) for x in range(len(line))]
            list_of_val_arr = np.array(list_values)
            max_list_val = np.max(list_values)
        line = line.split()
        if len(line) ==0:
            hash_table = np.zeros(max_list_val)
            list_of_objects.append((hash_table, np.array(current_list)))
            current_list =[]
        else: 
            current_list.append(line)
    list_of_objects[0] = list_of_val_arr
    return list_of_objects


def insert_hash_per_list(data):
    for hash_, lis in data[1:]: 
        for element in lis:
            list_indicis = list(map(int, element))
            hash_[list_indicis] += np.ones(1)
    return data
        
def is_done(arr, num):
    state = False
    hash_table, table = arr
    
    if hash_table[num] != np.ones(1): # check this
        # add to hash
        hash_table[num] += np.ones(1)
        
        # cheack row 
        for row in arr: 
            count = 0
            for curr_num in row: 
                if hash_table[curr_num] ==np.ones(1):
                    count+=1
                if(count ==len(row)): return True
                
        # Check colomn
        for col in range(5):
            corr_col = arr[:,col].T
            
            for curr_col_num in corr_col:
                count = 0
                if hash_table[curr_num] ==np.ones(1):
                    count+=1
                if(count ==len(row)): return True
        
    return False
                
def if_done(topule):
    pass            


def learning(data):
    done = False
    list_numbers, boards = data[0], data[1:]
    for num in list_numbers:
         for topule in boards:
             if (is_done(topule, num)):
                 
    



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)



path  = "C:/Users/admin/Documents/GitHub/Avent_Of_Code_Challenge_2021/Data_sets/data_4.txt"
data = open_file(path, 'r')

list_object= split_data(data)
hashed_list = insert_hash_per_list(list_object)

ss = 4