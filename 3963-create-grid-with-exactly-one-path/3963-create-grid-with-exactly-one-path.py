class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m==1 or n==1:
            sol=[['.' for i in range(n)] for i in range(m)]
            ans=[]
            for i in sol:
                ans.append(''.join(i))
            return ans
        sol=[['#' for i in range(n)] for i in range(m)]
        i=0
        j=0
        k=True
        while True:
            sol[i][j]='.'
            if i==m-1 and (i,j)!=(m-1,n-1):
                i,j=i,j+1
            elif j!=n-1:
                if k:
                    i,j=i,j+1
                    k=False
                else:
                    i,j=i+1,j
                    k=True
            else:
                i,j=i+1,j
            if (i,j)==(m-1,n-1):
                sol[i][j]='.'
                ans=[]
                for i in sol:
                    ans.append(''.join(i))
                return ans
