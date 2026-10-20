class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        ans=0
        pre=skill[0]+skill[len(skill)-1]
        while i<j:
            cur=skill[i]+skill[j]
            if cur!=pre:
                print(cur,pre)
                print(i,j)
                return -1
            pre=cur
            ans+=skill[i]*skill[j]
            i+=1
            j-=1
        return ans