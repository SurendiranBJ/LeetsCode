class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        sol=0
        key=1
        for i in range(len(word)):
            sol+=key
            if (i+1)%8==0:
                key+=1
        return (sol)        