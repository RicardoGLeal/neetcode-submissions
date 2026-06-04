# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Shared scoreboard — updated every time we find a longer path
        res = 0

        def dfs(root):
            nonlocal res

            # Base case: empty node contributes 0 height
            if not root:
                return 0

            # Recurse first — we need the heights from below
            # before we can evaluate the path through this node
            left  = dfs(root.left)
            right = dfs(root.right)

            # At this node, the longest path through it = left arm + right arm.
            # Update the scoreboard if this beats the best seen so far.
            res = max(res, left + right)

            # Tell the parent how tall this subtree is.
            # The parent only cares about the longer arm (+ 1 for the edge to this node).
            return 1 + max(left, right)

        dfs(root)
        return res