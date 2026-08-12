class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2<=100:
            return 0
        c=0    
        for i in range(num1,num2+1):
            l=len(str(i))
            s=str(i)
            for i in range(1,l-1):
                if int(s[i])>int(s[i-1]) and int(s[i])>int(s[i+1]):
                    c+=1
                elif int(s[i])<int(s[i-1]) and int(s[i])<int(s[i+1]):
                    c+=1
        return c    