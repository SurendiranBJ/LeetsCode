# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        ans=0
        k=False
        def tree(root,v):
            nonlocal k
            if root:
                if not root.right and not root.left:
                    v+=root.val
                    print(v)
                    if v==targetSum:
                        print(99)
                        k=True
                        print(k)
                        return 
                    else:
                        return
                if root.left:
                    tree(root.left,v+root.val)
                if root.right:
                    tree(root.right,v+root.val)
        if not root:
            return False
        tree(root,0)
        return k
                