class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        visi=set()
        r=len(grid)
        c=len(grid[0])
        pr,pc=0,0
        cr,cc=0,0
        while not (cr>=r or cc<0 or cr<0 or cc>=c or (cr,cc)in visi):
            visi.add((cr,cc))
            if grid[cr][cc]=='R':
                pr,pc=cr,cc
                cr,cc=cr,cc+1
            elif grid[cr][cc]=='L':
                pr,pc=cr,cc
                cr,cc=cr,cc-1
            elif grid[cr][cc]=='U':
                pr,pc=cr,cc
                cr,cc=cr-1,cc
            else:
                pr,pc=cr,cc
                cr,cc=cr+1,cc
        return [pr,pc]

        