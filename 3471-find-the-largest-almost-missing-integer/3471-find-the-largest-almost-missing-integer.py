class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        di={}
        for i in range(0,len(nums)-k+1):
            li=nums[i:i+k]
            p=set()
            for j in li:
                if j not in di:
                    di[j]=1
                    p.add(j)
                elif j not in p:
                    di[j]+=1
                    p.add(j)

        sol=[]
        for key,value in di.items():
            if value==1:
                sol.append(key)
        if len(sol)==0:
            return -1
        else:
            return max(sol)            