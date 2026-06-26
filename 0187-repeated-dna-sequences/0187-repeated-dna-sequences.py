class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        if len(s)<10:
            return []
        k=10
        di={}
        st=''
        for i in range(k):
            st+=s[i]

        di[st]=di.get(st,0)+1
        for i in range(k,len(s)):
            st=s[i-k+1:i-k+10+1]
            print(st)
            di[st]=di.get(st,0)+1
            if di[st]>1:
                if st not in ans:
                    ans.append(st)
        return ans        