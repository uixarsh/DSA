# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        lft_node = self.maxDepth(root.left)
        rgt_node = self.maxDepth(root.right)
        
        return 1 + max(lft_node, rgt_node)