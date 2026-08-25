class Solution:
    def isPalindromic(self, s: str) -> bool:
        sol=''
        for i in s:
            sol+=format(ord(i),'08b')

        if sol==sol[::-1]:
            return True
        else:
            return False      