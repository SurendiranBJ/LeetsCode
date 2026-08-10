class Solution:
    def removeStars(self, s: str) -> str:
        li=[]
        for i in s:
            if i=='*' and len(li)>0:
                li.pop(-1)
            else:
                li.append(i)
        return ''.join(li)            