class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans=0
        for i in sentences:
            l=len(i.split())
            ans=max(l,ans)
        return ans    
