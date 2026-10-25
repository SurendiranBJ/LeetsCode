class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        al=['op','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans=''
        for i in range(26,0,-1):
            while k-i>=(n-1) and n!=0:
                k-=i
                ans+=al[i]
                n-=1
        return ans[::-1]