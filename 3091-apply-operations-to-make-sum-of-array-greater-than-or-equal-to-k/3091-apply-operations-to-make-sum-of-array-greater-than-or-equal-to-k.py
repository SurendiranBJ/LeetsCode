class Solution:
    def minOperations(self, k: int) -> int:
        sum=1
        ans=0
        for i in range(2,k):
            sum+=1
            ans+=1
            if i*i>=k:
                print(i*i)
                break   
        z=sum
        while sum<k:
            ans+=1
            sum+=z

        return ans
