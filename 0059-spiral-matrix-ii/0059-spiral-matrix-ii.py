class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[[0]*n for i in range(n)]
        right=n-1
        left=0
        top=0
        bottom=n-1
        c=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans[top][i]=c
                c+=1
            top+=1
            for i in range(top,bottom+1):
                ans[i][right]=c
                c+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans[bottom][i]=c
                    c+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans[i][left]=c
                    c+=1
                left+=1
        return ans               