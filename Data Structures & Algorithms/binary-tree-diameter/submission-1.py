# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # An empty tree has no path, so diameter is 0
        if not root:
            return 0

        # Get the height of each subtree rooted at the current node's children.
        # These represent the two "arms" of the longest path passing through root.
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)

        # The longest path THROUGH this node = left arm + right arm.
        # (e.g. some deep left leaf → root → some deep right leaf)
        diameter = leftHeight + rightHeight

        # But the diameter might not pass through this node at all.
        # It could be entirely inside the left or right subtree.
        # So we recurse down and ask each subtree: "what's YOUR best diameter?"
        sub = max(self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right))

        # Return whichever is longer: the path through this node, or the best found below
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        # An empty subtree contributes 0 edges
        if not root:
            return 0

        # Height = 1 (edge to this node) + the taller of the two subtrees below.
        # This recurses all the way down to the leaves, then builds the answer back up.
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))