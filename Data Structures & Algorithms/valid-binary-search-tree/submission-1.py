# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            # Base case: empty node is always valid
            if not node:
                return True
            
            # Current node must fall strictly within the inherited bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Left subtree: tighten the upper bound to current node's value
            # Right subtree: tighten the lower bound to current node's value
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # Start with no constraints — any value is valid at the root
        return dfs(root, float("-inf"), float("inf"))

        