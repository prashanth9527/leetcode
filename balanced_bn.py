# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if not root:
                return 0
            left=fun(root.left)
            right=fun(root.right)
            if left==-1 or right ==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return fun(root)!=-1