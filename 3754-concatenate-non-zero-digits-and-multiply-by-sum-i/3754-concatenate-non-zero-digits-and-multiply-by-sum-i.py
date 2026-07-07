class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=''
        for i in str(n):
            if i!='0':
                x+=i

        s=0
        if x=='':
            return 0
        for i in x:
            s+=int(i)        
        return int(x)*s        