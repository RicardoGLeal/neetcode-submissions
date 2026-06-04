# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                # Both targets are smaller, so LCA must be in the left subtree
                node = node.left
            elif p.val > node.val and q.val > node.val:
                # Both targets are larger, so LCA must be in the right subtree
                node = node.right
            else:
                # The two targets diverge here (or one of them IS this node),
                # so this is the lowest point where both are reachable — the LCA
                return node
