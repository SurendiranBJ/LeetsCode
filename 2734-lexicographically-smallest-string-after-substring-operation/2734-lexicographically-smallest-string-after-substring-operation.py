class Solution:
    def smallestString(self, s: str) -> str:
        ans=""
        i=0
        l=len(s)
        if l==1 and s[0]=='a':
            return 'z'
        while i<l and s[i]=='a':
            i+=1
            ans+='a'
            if i==l-1:
                if s[i]=='a':
                    ans+='z'
                    return ans
        while i<l and s[i]!='a':
            ans+=(chr(ord(s[i])-1))
            i+=1
        return ans+s[i:]