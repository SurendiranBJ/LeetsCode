# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        sum=0
        def tree(root,value):
            nonlocal sum
            if root:
                if not root.left and not root.right:
                    value+=str(root.val)
                    sum+=int(value)
                    return
                if root.left:
                    tree(root.left,value+str(root.val))
                if root.right:
                    tree(root.right,value+str(root.val))
        tree(root,'')
        return sum