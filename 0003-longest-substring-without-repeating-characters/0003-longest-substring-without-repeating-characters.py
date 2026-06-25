class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=='':
            return 0
        ans=0
        di={}
        left=0
        for right in range(len(s)):
            di[s[right]]=di.get(s[right],0)+1
            while di[s[right]]>1:
                di[s[left]]-=1
                if di[s[left]]==0:
                    del di[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans                    