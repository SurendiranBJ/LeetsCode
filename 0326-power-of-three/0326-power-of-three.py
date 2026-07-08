class Solution(object):
    key=False
    def sol(self,n,x):
        global key
        if n%3!=0:
            return
        if n<3:
            return
        if n==3**x:
            self.key=True
            return
        if 3**x>n:
            return     
        self.sol(n,x+1)
        return    
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        global key
        self.sol(n,1)
        if n==1:
            return True
        if self.key:
            return True
        else:
            return False    
        