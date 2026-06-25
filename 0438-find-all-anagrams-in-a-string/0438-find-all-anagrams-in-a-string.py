from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans=[]
        k=len(p)
        if k>len(s):
            return []
        di={}
        p=Counter(p)
        for i in range(k):
            di[s[i]]=di.get(s[i],0)+1
        if p==di:
            ans.append(0)
        for i in range(k,len(s)):
            di[s[i-k]]-=1
            if di[s[i-k]]==0:
                del di[s[i-k]]
            di[s[i]]=di.get(s[i],0)+1
            if p==di:
                ans.append(i-k+1)
        return ans            
