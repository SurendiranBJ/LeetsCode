class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        right=n-1
        left=0
        top=0
        bottom=m-1
        c=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
                c+=1
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
                c+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                    c+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                    c+=1
                left+=1
        return ans               