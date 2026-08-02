class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        given=a/b
        ans=0
        for i in range(len(nums)):
            sol=[]
            x=0
            y=0
            for j in range(i,len(nums)):
                sol.append(nums[j])
                if nums[j]%2==0:
                    x+=1
                else:
                    y+=1    
                if y>0:
                    if x/y <=a/b:
                        ans+=1
        return ans