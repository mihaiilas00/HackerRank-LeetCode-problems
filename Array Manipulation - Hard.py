################################################################################################################
#Problem:
#   Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive.
#   Once all operations have been performed, return the maximum value in the array.
#Function Description
#   Complete the function arrayManipulation.
#   arrayManipulation has the following parameters:
#       int n - the number of elements in the array
#       int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
#Returns
#   int - the maximum value in the resultant array
#Input Format
#   The first line contains two space-separated integers  and , the size of the array and the number of operations.
#   Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.
#
#Author: Mihai Ilas
###################################################################################################################

import math
import os
import random
import re
import sys
from operator import itemgetter

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    list_starts=queries[:]
    list_stops=queries[:]
    list_starts.sort(key=itemgetter(0))
    list_stops.sort(key=itemgetter(1))
    summ = 0
    maxi = -1
    stop_flag = 0
    start_flag = 0
    
    for i in range(n):
        switch_on = 0
        switch_off = 0
        if start_flag < len(queries):
            while ((switch_on and switch_off) == False):
                if i == list_starts[start_flag][0]-1:
                    switch_on = 1 
                    summ += list_starts[start_flag][2]
                    start_flag += 1
                if switch_on == 0: break
                if start_flag == len(queries): break
                if switch_on == 1 and i != list_starts[start_flag][0]-1:
                    switch_off = 1
                    
        switch_on = 0
        switch_off = 0
        
        if stop_flag < len(queries):
            while ((switch_on and switch_off) == False):
                if i == list_stops[stop_flag][1]: 
                    summ -= list_stops[stop_flag][2]
                    stop_flag += 1
                    switch_on = 1 
                if switch_on == 0: break
                if stop_flag == len(queries): break
                if switch_on == 1 and i != list_stops[stop_flag][1]:
                    switch_off = 1
                    
        if summ>maxi: maxi = summ
        if start_flag == len(queries) and stop_flag == len(queries): return maxi
        

    return maxi


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
