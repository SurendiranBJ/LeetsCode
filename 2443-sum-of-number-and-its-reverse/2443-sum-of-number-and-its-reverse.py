class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        for i in range(0,num):
            s=str(i)
            if i+int(s[::-1])==num:
                return True
        return False        