# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(x,y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            
            return check(x.left,y.right) and x.val==y.val and check(x.right,y.left)
        return check(root.left,root.right)

        