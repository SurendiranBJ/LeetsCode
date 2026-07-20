class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        for l in range(k):
            a=grid[0].pop()
            for i in range(1,m):
                 grid[i].insert(0,a)
                 a=grid[i].pop()
            grid[0].insert(0,a)     
        return grid    