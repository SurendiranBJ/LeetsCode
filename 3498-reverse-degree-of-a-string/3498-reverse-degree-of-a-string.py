class Solution:
    def reverseDegree(self, s: str) -> int:
        apl=[chr(i) for i in range(97,123)]
        apl=apl[::-1]
        
        ans=0
        for i in range(len(s)):
            idx=apl.index(s[i])+1
            ans+=((i+1)*idx)
        return ans 