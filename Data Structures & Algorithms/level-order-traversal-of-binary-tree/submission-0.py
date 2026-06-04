# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:  # process until no more nodes remain
            level = []

            # len(queue) is snapshot of current level's node count;
            # new children appended during this loop won't affect the range
            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)   # append even if None; filtered above
                    queue.append(node.right)  # same

            # only add to result if level has real nodes (guards against null children)
            if level:
                res.append(level)
        return res