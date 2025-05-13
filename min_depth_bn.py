# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[]
        depth=1
        q.append((root,depth))
        while q:
            cur,dep=q.pop(0)
            if not cur.left and not cur.right:
                return dep
            if cur.left:
                q.append((cur.left,dep+1))
            if cur.right:
                q.append((cur.right,dep+1))
        return dep


        