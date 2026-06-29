class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        ans=0
        word=str(word)
        for i in patterns:
            if i in word:
                ans+=1
        return ans        