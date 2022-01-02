import os
import numpy

""" 
Helper function:
Import
"""

def importdata_(path, operation):
        with open(path, operation) as file_1:
            read_data = file_1.readlines()
            return read_data