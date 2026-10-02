import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        ans=[]
        def dfs(root):
            nonlocal ans
            ans.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        ans=sorted(list(set(ans)))
        if len(ans)==1:
            return -1
        else:
            return ans[1]