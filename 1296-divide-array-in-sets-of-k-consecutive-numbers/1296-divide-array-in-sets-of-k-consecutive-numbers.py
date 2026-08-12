from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        c = Counter(nums)

        for x in sorted(c):
            if c[x] == 0:
                continue

            count = c[x]

            for i in range(x, x + k):
                if c[i] < count:
                    return False
                c[i] -= count

        return True