class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        one=s.count('1')
        zero=s.count('0')
        if one==0 or zero==0:
            return 1
        
        for i in range(len(s)):
            sol=s[:i+1]
            one=sol.count('1')
            zero=sol.count('0')
            if (one==0 or zero==0) and len(sol)>1:
                continue
            if abs(one-zero)==1 or abs(one-zero)==0:
                print(sol)
                ans+=1
        return ans 