class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()
        t=s.split(" ")
        ans=[]
        for i in t[::-1]:
            if len(i)==0:
                continue
            else:
                p=''.join(i)
                ans.append(p)
        return ' '.join(ans)        

        
        