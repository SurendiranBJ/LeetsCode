from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        for i in strs:
            t=sorted(list(i))
            t=''.join(t)
            if t in di:
                di[t].append(i)
            else:
                di[t]=[]
                di[t].append(i)
        ans=[]
        for i,j in di.items():
            ans.append(j)     
        return ans      