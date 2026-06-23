class Solution(object):
    def reverseVowels(self, s):
       
        """
        :type s: str
        :rtype: str
        """
        v=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        i=0
        j=len(s)-1
        
        while (i<j):
            print(1)
            if s[i] in v and s[j] in v:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in v and s[j] not in v:
                j-=1
            elif s[i] not in v and s[j] in v:
                i+=1
            else:
                i+=1
                j-=1    
        return ''.join(s)            