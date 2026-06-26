class Solution(object):
    def s(self,li,i,n,k):
        j=i
        su=0
        c=0
        j+=1
        while j!=i:
            if c==k:
                break
            if j==n:
                j=0
              
            su+=li[j]
            c+=1
            j+=1
        return su
    def s1(self,li,i,n,k):
        j=i
        su=0
        c=0
        j-=1
        while j!=i and c!=k:
            if j<0:
                j=n-1
               
            su+=li[j]
            c+=1
            j-=1
        return su               
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[0]*len(code)
        if k>0:
            for i in range(len(code)):
                ans[i]=self.s(code,i,len(code),k)
            return ans
        elif k<0:
            for i in range(len(code)):
                ans[i]=self.s1(code,i,len(code),abs(k))
            return ans
        elif k==0:
            return [0]*len(code)    
                    