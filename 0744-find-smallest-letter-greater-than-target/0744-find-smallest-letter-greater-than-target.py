class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        c=ord(target)
        for i in letters:
            if ord(i)>c:
                return i
        return letters[0]        