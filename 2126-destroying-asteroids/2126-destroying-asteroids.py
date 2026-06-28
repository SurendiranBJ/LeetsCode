class Solution(object):
    def asteroidsDestroyed(self, mass, ast):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        ast.sort()
        i=0
        while i<len(ast):
            if mass>=ast[i]:
                mass+=ast[i]
                i+=1
            else:
                return False
        return True            