from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        k=len(s1)
        if len(s1)>len(s2):
            return False
        s1=Counter(s1)
        di={}
        for i in range(k):
            di[s2[i]]=di.get(s2[i],0)+1
        if di==s1:
            return True
        for i in range(k,len(s2)):
            di[s2[i-k]]-=1
            if di[s2[i-k]]==0:
                del di[s2[i-k]]  
            di[s2[i]]=di.get(s2[i],0)+1
            if di==s1:
                return True
        return False                       
