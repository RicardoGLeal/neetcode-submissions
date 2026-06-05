# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # countdown: when it hits 0 we've visited the kth node
        cnt = k
        # safe default — will always be overwritten before we return
        res = root.val

        def dfs(node):
            nonlocal cnt, res

            # base case: went past a leaf, nothing to do
            if not node:
                return

            # 1) visit entire left subtree first (inorder: left → self → right)
            dfs(node.left)

            # 2) if answer was already found somewhere in the left subtree, stop
            #    — no need to process this node or go right
            if cnt == 0:
                return

            # 3) "visit" this node: count it toward k
            cnt -= 1

            # 4) this node is exactly the kth — record and stop
            if cnt == 0:
                res = node.val
                return

            # 5) answer not found yet, so it must be in the right subtree
            dfs(node.right)

        dfs(root)
        return res



