# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        sol=[]
        z=0
        def update(root):
            nonlocal z
            if root:
                update(root.left)
                root.val=ans[z]
                z+=1
                update(root.right)
        def dfs(root):
            nonlocal sol
            if root:
                dfs(root.left)
                sol.append(root.val)
                dfs(root.right)
        dfs(root)
        ans=[0]*len(sol)
        ans[len(sol)-1]=sol[len(sol)-1]
        for i in range(len(sol)-2,-1,-1):
            ans[i]=sol[i]+ans[i+1]
        update(root)
        return root