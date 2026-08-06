class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            li=[int(i) for i in str(i)]
            if math.prod(li)%t==0:
                return i