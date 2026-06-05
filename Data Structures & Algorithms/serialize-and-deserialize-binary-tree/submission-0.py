# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            # Base case: null node gets a sentinel marker
            # without this, we can't distinguish a leaf from an internal node during deserialization
            if not node:
                return "null"

            # Preorder: process current node first, then left subtree, then right
            # each recursive call returns the fully serialized string of that subtree
            # so we just concatenate: current value + left result + right result
            return str(node.val) + ", " + dfs(node.left) + ", " + dfs(node.right)
        return dfs(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the string back into individual tokens and load into a deque
        # deque gives us O(1) popleft() — a regular list would be O(n) per pop from the front
        tokens = deque(data.split(", "))

        def dfs():
            # Consume the next token — this advances the shared pointer for all recursive calls
            # because tokens is defined in the outer scope and mutated (not rebound), 
            # all calls share the same deque automatically
            val = tokens.popleft()

            # Base case: sentinel means this subtree is empty
            if val == "null":
                return None

            # Preorder mirrors serialize: build current node first, then recurse left then right
            # left call consumes however many tokens its subtree needs,
            # so right call automatically starts at the correct position
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
