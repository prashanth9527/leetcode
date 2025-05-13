# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        c=0
        q=deque([root,1])
        while q:
            x,dep=q.popleft()
            if x.left:
                q.append(x.left,dep+1)
            if x.right:
                q.append(x.right,dep+1)
        return min(left,right)


        