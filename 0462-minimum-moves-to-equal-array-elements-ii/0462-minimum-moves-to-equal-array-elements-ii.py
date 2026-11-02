class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        ans=0
        for i in nums:
            if i!=mid:
                if i<mid:
                    if i<0:
                        ans+=(-(i))
                        if mid!=0:
                            ans+=mid
                    else:
                        ans+=(mid-i)
                else:
                    ans+=(i-mid)
        return ans
