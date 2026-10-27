# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        height=0
        def map(root,x,y):
            nonlocal sol
            if root:
                if root.left:
                    r=x+1
                    c=y-2**((height)-r-1)
                    print(r,c)
                    sol[r][c]=str(root.left.val)
                    map(root.left,r,c)
                if root.right:
                    r=x+1
                    c=y+2**((height)-r-1)
                    sol[r][c]=str(root.right.val)
                    map(root.right,r,c)


        def hei(root,depth):
            nonlocal height
            if root:
                if root.left:
                    hei(root.left,depth+1)
                height=max(height,depth)
                if root.right:
                    hei(root.right,depth+1)
                height=max(height,depth)
        hei(root,1)
        sol=[["" for i in range(((2**(height)-1)))] for i in range(height)]
        sol[0][((2**(height)-1)//2)]=str(root.val)
        map(root,0,((2**(height)-1)//2))
        return sol