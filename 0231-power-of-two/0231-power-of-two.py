class Solution(object):
    key=False
    def sol(self,n,x):
        if n%2!=0 or n<2 or 2**x>n:
            return
        if n==2**x:
            self.key=True
            return     
        self.sol(n,x+1)
        return    
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        self.sol(n,1)
        if self.key:
            return True
        else:
            return False  