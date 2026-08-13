class Solution:
    def minCost(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 1
        if n==3:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            dp[i]=i+(dp[i-1]-1)
        return dp[n]        