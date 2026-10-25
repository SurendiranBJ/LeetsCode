class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        i=0
        j=2
        if s1==s2:
            return True
        while j<4:
            if s1[i]!=s2[i] and s1[j]!=s2[j]:
                s1[i],s1[j]=s1[j],s1[i]
                if s1==s2:
                    return True
            i+=1
            j+=1
        return False