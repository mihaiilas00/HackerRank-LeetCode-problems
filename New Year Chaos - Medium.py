#################################################################################################
#It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
#Each person wears a sticker indicating their initial position in the queue.
#Initial positions increment by  from  at the front of the line to  at the back.
#
#Any person in the queue can bribe the person directly in front of them to swap positions.
#If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. 
#
#Author: Mihai Ilas
#
################################################################################################

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    flag = 0
    for i in range(n-1,0,-1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                a = q[i]
                q[i] = q[i-1]
                q[i-1] = a
                ans += 1
            elif q[i-2] == i+1:
                a = q[i-2]
                q[i-2] = q[i-1]
                q[i-1] = a
                a = q[i-1]
                q[i-1] = q[i]
                q[i] = a
                ans += 2
            else: 
                print ("Too chaotic")
                flag = 1
                break
    if flag == 0: print(ans)

                

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
