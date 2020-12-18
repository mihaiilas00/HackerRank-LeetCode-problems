####################################################################################################################
#Consider a matrix where each cell contains either a  or a  and any cell containing a  is called a filled cell.
#Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally.
#
#If one or more filled cells are also connected, they form a region.
#Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.
#
#Given an  matrix, find and print the number of cells in the largest region in the matrix.
#
#Author: Mihai Ilas
#
####################################################################################################################

import math
import os
import random
import re
import sys

counter=0
visited=[[]]

def dfs(x,y,mat):
    global counter
    global visited
    visited[x][y] = 1
    counter += 1 
    
    if x < len(mat)-1:
        if mat[x+1][y] == 1 and visited[x+1][y] == 0 :
            dfs(x+1,y,mat)
            
    if y < len(mat[0])-1:
        if mat[x][y+1] == 1 and visited[x][y+1] == 0:
            dfs(x,y+1,mat)
            
    if x > 0:
        if mat[x-1][y] == 1 and visited[x-1][y] == 0: 
            dfs(x-1,y,mat)
            
    if y > 0:
        if mat[x][y-1] == 1 and visited[x][y-1] == 0:
            dfs(x,y-1,mat)
            
    if x < len(mat)-1 and y < len(mat[0])-1:
        if mat[x+1][y+1] == 1 and visited[x+1][y+1] == 0:
            dfs(x+1,y+1,mat)
            
    if x < len(mat)-1 and y > 0:
        if mat[x+1][y-1] == 1 and visited[x+1][y-1] == 0 :
            dfs(x+1,y-1,mat)
            
    if x > 0 and y > 0:
        if mat[x-1][y-1] == 1 and visited[x-1][y-1] == 0:
            dfs(x-1,y-1,mat)
            
    if x > 0 and y < len(mat[0])-1:
        if mat[x-1][y+1] == 1 and visited[x-1][y+1] == 0:
            dfs(x-1,y+1,mat)
      
    

# Complete the maxRegion function below.
def maxRegion(grid):
    maximum=0
    global counter
    global visited
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                visited=[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
                counter=0
                dfs(i,j,grid)
                maximum=max(maxi,counter)
                
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    m = int(raw_input())

    grid = []

    for _ in xrange(n):
        grid.append(map(int, raw_input().rstrip().split()))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
