# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:  # Base case: if the tree is empty
            return 0
        
        # Recursive calls for left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is the greater of the two, plus one
        return max(left_depth, right_depth) + 1