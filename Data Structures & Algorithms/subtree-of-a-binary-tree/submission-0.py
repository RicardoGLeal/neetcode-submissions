# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Checks if two trees are identical in structure and values
        def isSameTree(s, t):
            # Both null means we've matched all the way to the leaves
            if not s and not t:
                return True
            # One null, one not — structures diverge
            if not s or not t:
                return False
            # Current values must match, then recurse on both sides
            return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Exhausted root without finding a match
        if not root:
            return False

        # Try matching subRoot at the current node,
        # then fall back to searching left and right subtrees
        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
