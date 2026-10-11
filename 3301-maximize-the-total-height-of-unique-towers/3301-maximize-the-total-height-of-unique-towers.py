class Solution:
    def maximumTotalSum(self, height: List[int]) -> int:
        height.sort(reverse=True)
        ans=height[0]
        pre=height[0]
        for i in range(1,len(height)):
            print(pre)
            if height[i]<pre:
                ans+=height[i]
                pre=height[i]
            else:
                k=pre-1
                if k>0:
                    ans+=k 
                    pre=k
                else:
                    return -1     
        return ans            