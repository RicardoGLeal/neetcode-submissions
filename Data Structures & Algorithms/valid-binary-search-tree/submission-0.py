# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, interval):
            if not root:
                return True
            
            minVal = interval[0]
            maxVal = interval[1]

            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return dfs(root.left, [minVal, root.val]) and dfs(root.right, [root.val, maxVal])

        
        if not root:
            return True
        
        return dfs(root.left, [float("-inf"), root.val]) and dfs(root.right, [root.val, float("inf")])

        