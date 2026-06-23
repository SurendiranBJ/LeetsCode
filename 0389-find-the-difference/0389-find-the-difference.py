class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sa=[]
        ta=[]
        for i in s:
            sa.append(i)
        for j in t:
            ta.append(j)
        ans=""
        for i in sa:
            if i in ta:
                ta.remove(i)
            else:
                ans+=i
        for i in ta:
            ans+=i
        return ans
            