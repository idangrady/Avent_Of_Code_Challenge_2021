#from Day_1 import open_file
import sys, os
import numpy as np

def open_file(filename, operation):
    with open(filename, operation) as file_1:
        read_data = file_1.readlines()
        return read_data


def split_data(data):
    list_of_objects = []
    current_list = []
    hash_table = []
    for idx, line in enumerate(data):
        if idx==0:
            list_values = []
            prev = ''
            for i in line:
                if i ==',':
                    list_values.append(int(prev))
                    prev = ''
                elif(i.isdigit()): 
                    prev+=i

            list_of_val_arr = np.array(list_values)
            max_list_val = np.max(list_values) +1
        line = line.split()
        if len(line) ==0:
            hash_table = np.zeros([max_list_val,3])
            list_of_objects.append((hash_table, np.array(current_list), [[] for x in range(5)],[[] for x in range(5)]))
            current_list =[]
        else: 
            current_list.append(line)
    list_of_objects[0] = list_of_val_arr
    return list_of_objects, list_values


def if_done(board, num):
     hash_ , lis, row_values, col_values = board
     flattened_col  = [int(val) for sublist in col_values for val in sublist]
     flattened_row  = [int(val) for sublist in row_values for val in sublist]
     merged_  = flattened_col+flattened_row

     count = 0
     all_indexed = hash_[hash_[0:]==1]
     #find all the values which have not been called yet
     for row in lis:
        for item in row: 
            item = int(item)
            if item not in merged_:
                count += item
 
     return(num * count)
     
    


def insert_hash_per_list(data):
    ss = 2
    for  hash_, lis,_,_ in (data[1:]): 
        for row,element in enumerate(lis):
            list_indicis = list(map(int, element))
            for col, item in enumerate(list_indicis):
                hash_[item] = [1, row,col]
    return data
        
def is_done(arr, num, target):
    state = False
    hash_table, table,row_table, col_table = arr
    
    if hash_table[num,0] != 0: # check this
        row_loc, col_loc = list(hash_table[num,1:])
        row_loc = int(row_loc)
        col_loc = int(col_loc)
        
        if( num not in row_table[row_loc] and num not in col_table[col_loc]):
            # we encounter for the first time
            row_table[row_loc].append(int(num))
            col_table[col_loc].append(int(num))
            
            # check if we we have a series of 5 ==> done
            if(len(row_table[row_loc])==target):
                state = True
                return(row_table[row_loc])
            elif(len(col_table[col_loc])==target):
                state = True
                return(col_table[col_loc])

    return state
   


def learning(data):
    done = False
    list_numbers, boards = data[0], data[1:]
    for num in list_numbers:
         for topule in boards:
             if (is_done(topule, num)):
                 pass
                 
    



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)



path  = "/Users/idangrady/Documents/GitHub/Avent_Of_Code_Challenge_2021/Data_sets/data_4.txt"
data = open_file(path, 'r')

list_object, list_values= split_data(data)
hashed_list = insert_hash_per_list(list_object)

numbers = hashed_list[0]

last_board = 0
target = 5

reminding = []

for num in list_values:
    for  board in (hashed_list[1:]):
        if (board not in reminding):
            state = is_done(board, num, target)
            if(state):
                print(state)
                print("finish")
                score = if_done(board, num)
                last_board = score
                reminding.append(board[1])
            
            

print(last_board)


