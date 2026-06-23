class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a,b=word1,word2
        m=min(len(a),len(b))
        ans=''
        i=0
        while i<=m-1:
            ans=ans+a[i]+b[i]
            i+=1
        if m==len(a):
            ans+=b[m:] 
        elif m==len(b):
            ans+=a[m:]
        return ans           