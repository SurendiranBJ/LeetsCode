class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)<k:
            return 0
        v='aeiou'
        count=0
        ans=0      
        for i in range(k):
            if s[i] in v:
                count+=1
        ans=count        
        for i in range(k,len(s)):
            if s[i-k] in v:
                count-=1
            if s[i] in v:
                count+=1
            ans=max(ans,count)
        return ans            