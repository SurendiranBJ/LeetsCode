class Solution(object):
    key=False
    def sol(self,n,x):
        if n%3!=0 or n<3 or 3**x>n:
            return
        if n==3**x:
            self.key=True
            return     
        self.sol(n,x+1)
        return    
    def isPowerOfThree(self, n):
        if n==1:
            return True
        self.sol(n,1)
        if self.key:
            return True
        else:
            return False    