import copy
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans=0
        c=copy.deepcopy(colors)
        c+=colors
        c+=colors
        for i in range(len(colors),len(colors)+len(colors)):
            if c[i]==1:
                if c[i-1]==0 and c[i+1]==0:
                    ans+=1
            else:
                if c[i-1]==1 and c[i+1]==1:
                    ans+=1
        return ans