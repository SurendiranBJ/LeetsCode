from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans=[]
        c=Counter(nums)
        sol=[]
        key=False
        for i in range(lower,upper+1):
            if i not in c and not key:
                sol.append(i)
                key=True
            elif i in c:
                if len(sol)==1:
                    print(i)
                    sol.append(i-1)
                    key=False
                    ans.append(sol)
                    sol=[]
        if len(sol)==1 and upper not in c:
            sol.append(upper)
            ans.append(sol)
        elif len(sol)==1 and upper in c:
            sol.append(sol[0])
            ans.append(sol)
        return ans