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

# Preorder: 8 → 3 → 1 → 6 → 4 → 7 → 10 → 14 → 13
# Inorder: 1 → 3 → 4 → 6 → 7 → 8 → 10 → 13 → 14

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case: if either list is empty, there's nothing to build
        if not preorder or not inorder:
            return None

        indices = {}
        for idx,val in enumerate(inorder):
            indices[val] = idx

        # the root is always the first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # find where the root sits in inorder
        # everything to its left = left subtree, everything to its right = right subtree
        mid = indices[root_val]

        # split inorder around the root
        left_inorder  = inorder[:mid]       # left subtree nodes
        right_inorder = inorder[mid+1:]     # right subtree nodes (skip root itself)

        # split preorder using the SIZE of the left subtree we just found
        # preorder[0] is root, so left subtree starts at index 1
        # and spans exactly len(left_inorder) elements
        left_preorder  = preorder[1 : 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]   # whatever is left

        # recurse: each call returns the root of that subtree
        root.left  = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


        

