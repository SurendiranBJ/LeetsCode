class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]
        def findsol(li,sol,i):
            if len(sol)==k:
                ans.append(sol[:])
                return            
            if i<0 or i>n-1:
                return 
            sol.append(li[i])
            findsol(li,sol,i+1)
            sol.pop()
            findsol(li,sol,i+1)
            return
        li=[i for i in range(1,n+1)]
        findsol(li,[],0)
        return ans    