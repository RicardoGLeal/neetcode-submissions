# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the node is None, there's nothing to invert
        # This also handles the case where the tree is empty
        if not root:
            return None
        
        # Swap the left and right children of the current node
        # Python evaluates the right side fully before assigning,
        # so no temp variable is needed
        root.left, root.right = root.right, root.left

        # Recurse into the (already swapped) left subtree
        self.invertTree(root.left)

        # Recurse into the (already swapped) right subtree
        self.invertTree(root.right)

        # Return the root with its subtrees now fully inverted
        return root