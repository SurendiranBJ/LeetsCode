class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        li=[]
        ans=[]
        for i in range(len(s)):
            if s[i]==c:
                li.append(i)
        for i in range(len(s)):
            sol=[]
            for j in li:
                sol.append(abs(i-j))
            ans.append(min(sol))
        return ans        
