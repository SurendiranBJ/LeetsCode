import math
class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(variables)):
            a,b,c,d=variables[i][0],variables[i][1],variables[i][2],variables[i][3]
            sol=pow(pow(a,b,10),c,d)
            if sol==target:
                ans.append(i)
        return ans        