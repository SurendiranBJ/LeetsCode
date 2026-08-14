from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        di={}
        left=0
        for right in range(len(s)):
            di[s[right]]=di.get(s[right],0)+1
            while di[s[right]]>2 or di[s[left]]>2:
                di[s[left]]-=1
                if di[s[left]]==0:
                    del di[s[left]]
                left+=1    
            ans=max(ans,right-left+1) 
        return ans           