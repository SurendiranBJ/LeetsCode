from collections import deque
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sn=deque(sorted(nums))
        ans=0
        l=len(nums)
        n=deque(nums)
        if n==sn:
            return 0
        while sn!=n:
            n.rotate(1)
            ans+=1
            if ans>=l:
                return -1
        return ans  