class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        if amount==0:
            return 0
        dp=[[float('inf')]*(amount+1) for i in range(len(coins))]
        for j in range(len(coins)):
            dp[j][0]=0
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[i][j]=min(dp[i-1][j], 1+dp[i][j-coins[i]])
                else:
                    dp[i][j]=dp[i-1][j]                            
        if dp[len(coins)-1][amount]==float('inf'):
            return -1
        else:
            return dp[len(coins)-1][amount]  
        