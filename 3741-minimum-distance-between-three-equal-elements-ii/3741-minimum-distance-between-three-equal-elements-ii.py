from collections import Counter
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        di={}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]]=[]
                di[nums[i]].append(i) 
            else:
                di[nums[i]].append(i)
        sol=[]
        for i,j in di.items():
            if len(j)>=3:
                for k in range(0,len(j)-2):
                    sol.append(2 *((max(j[k], j[k+1], j[k+2]) - min(j[k], j[k+1], j[k+2]))))
        print(sol)
        if sol==[]:
            return -1
        else:
            sol.sort()
            return sol[0]
        