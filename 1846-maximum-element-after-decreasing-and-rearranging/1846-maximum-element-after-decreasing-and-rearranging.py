import numpy as np
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr[0]!=1:
            if arr[-1]==1:
                arr=arr[::-1]
            elif 1 in arr:
                idx=arr.index(1)
                arr[0],arr[idx]=arr[idx],arr[0]
            else:
                arr[0]=1        
        for j in range(1,len(arr)):
            if abs(arr[j]-arr[j-1])<=1:
                continue
            else:
                arr[j]=arr[j-1]+1  
        return max(arr)                        