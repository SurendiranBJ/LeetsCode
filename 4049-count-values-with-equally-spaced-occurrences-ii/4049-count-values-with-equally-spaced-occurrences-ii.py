from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        di={}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]]=[]
                di[nums[i]].append(i)
            else:
                di[nums[i]].append(i)
        ans=0
        for i,j in di.items():
            if len(j)>=3:
                print(i)
                sol=j[1]-j[0]
                l=True
                for k in range(len(j)-1):
                    if j[k+1]-j[k]!=sol:
                        l=False
                        break
                if l:

                    ans+=1
        return ans