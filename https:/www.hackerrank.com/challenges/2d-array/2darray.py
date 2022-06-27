#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
     # Write your code here
     
    rows, cols = (4, 4)
 
 
 
    output= [[0]*rows for _ in range(cols)]
    
    for i in range(0,4):
        for j in range(0,4):
           
    
        
            output[i][j]=arr[i][j+0]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j+0]+arr[i+2][j+1]+arr[i+2][j+2]
        
    
    return max(map(max, output)) 
        
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
