class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
            sol=format(i,'b')
            print(sol)
            ans.append(sol.count('1'))
        return ans    