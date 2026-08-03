class Solution:
    sol=set()
    for i in range(1,5000+1):
        b=format(i,'b')
        if b==b[::-1]:
            sol.add(i)
    def minOperations(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i in Solution.sol:
                ans.append(0)
            else:
                k=i+1
                l=i-1
                while True:
                    if k in Solution.sol:
                        ans.append(abs(i-k))
                        break
                    elif l in Solution.sol and l>0:
                        ans.append(abs(i-l))
                        break
                    k+=1
                    l-=1    
        return ans                  
