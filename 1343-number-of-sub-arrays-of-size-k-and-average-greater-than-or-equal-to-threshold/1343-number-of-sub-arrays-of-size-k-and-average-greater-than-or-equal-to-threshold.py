class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        if len(arr)<k:
            return 0
        ans=0
        s=0
        for i in range(k):
            s+=arr[i]
        if s/k>=threshold:
            ans+=1
        for i in range(k,len(arr)):
            s-=arr[i-k]
            s+=arr[i]
            if s/k>=threshold:
                ans+=1
        return ans                    