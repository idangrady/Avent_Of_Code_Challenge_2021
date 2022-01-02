import pandas as pd
import numpy as np
import math
import os
from helper_func import importdata_


class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 =y1
        self.x2= x2
        self.y2=y2
        
        self.lenth_x = int(math.fabs(self.x1- self.x2))+1
        self.lenth_y = int(math.fabs(self.y1- self.y2))+1
        
        
    def ver_hor(self):
        if self.x1 == self.x2 or self.y1 ==self.y2:
            return True
        else:
            return False
    
    def overlap(self, horizontal = True):
        x = np.linspace(self.x1, self.x2, self.lenth_x).reshape(-1,1)
        y = np.linspace(self.y1, self.y2, self.lenth_y).reshape(-1,1)

        if horizontal:
            if self.lenth_y<=1:
                y = np.zeros((self.lenth_x,1)) + int(self.y2)
            elif self.lenth_x<=1:
                x = np.zeros((self.lenth_y,1)) + int(self.x2)
            
            
        x_y = np.concatenate((x,y), axis = 1)
        return x_y

    

    
def clean_data(data):
    data_stript = [data[i].replace('->', ',').replace(' ', '').split(',') for i in range(len(data))]
    data_stript = [int(i) for sublist in data_stript for i in sublist]
    
    #
    return data_stript

def create_grid(data, d,n):
    arr = np.array(data).reshape(-1,n)
    points = [Point(x1, y1, x2, y2) for x1,y1,x2,y2 in arr]
    max_value = np.max(arr)
    grid = np.zeros((max_value, max_value))
    
    return grid, max_value, points

def fill_grid(grid,points, hor):
    
    for idx, point in enumerate(points):
        if hor:
            if(point.ver_hor()):
                maximu = np.maximum(point.lenth_x, point.lenth_y)
                for i in range(maximu):
                    try:
                        x,y = (point.overlap(horizontal = hor)[i])
                        grid[int(x),int(y)] +=1
                    except Exception as e:
                        pass
        else:
            maximu = np.maximum(point.lenth_x, point.lenth_y)
            for i in range(maximu):
                try:
                    x,y = (point.overlap(horizontal = hor)[i])
                    grid[int(x),int(y)] +=1
                except Exception as e:
                    pass
            
    return grid



if __name__ == "__main__":
    path= 'Data_sets/‏‏data_5.txt'
    data  = importdata_(path, 'r')
    
    data = clean_data(data)
    grid,_,points = create_grid(data, -1, 4)

    grid_1= fill_grid(grid,points, hor = True)
    
    answer_1 = np.where(grid_1>=2,1,0)
    print(print(f" Solution for part 1 Day 5: {answer_1.sum()}"))
    
    grid_2= fill_grid(grid,points, hor = False)
    
    answer_2 = np.where(grid_2>=2,1,0)
    print(print(f" Solution for part 2 Day 5: {answer_2.sum()}"))
