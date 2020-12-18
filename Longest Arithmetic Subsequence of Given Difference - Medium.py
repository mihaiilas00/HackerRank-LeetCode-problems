###################################################################
#Given an integer array arr and an integer difference,
#return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
#
#Author: Mihai Ilas
#
###################################################################

from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        k = difference
        dictionary = defaultdict(int)
        for i in range(len(arr)):
            dictionary[arr[i]] = 1+dictionary[arr[i]-k]
        maximum=1    
        for i in dictionary.values():
            if i > maximum: maximum = i    
        return maximum
