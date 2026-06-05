# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4   7 13

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left_gain  = max(dfs(node.left),  0)  # ignore negative arms
            right_gain = max(dfs(node.right), 0)

            # Best path through this node (can use both arms) → update global answer
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)

            # Return best single-arm extension to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum



            