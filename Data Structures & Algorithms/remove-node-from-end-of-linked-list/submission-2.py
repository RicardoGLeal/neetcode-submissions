# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node before head so left always has a predecessor to work with
        # this handles edge case of deleting the head node without special casing
        dummy = ListNode(0, head)
        left = dummy   # left trails behind — will stop at the node BEFORE the target
        right = head   # right scouts ahead to create the gap

        # ── Step 1: Advance right n steps ahead of left ───────────────────
        # this creates a fixed gap of n nodes between left and right
        # Example: n=2, list = 1 → 2 → 3 → 4 → 5
        #
        # after loop:
        # dummy → 1 → 2 → 3 → 4 → 5 → None
        #   ↑          ↑
        #  left      right        (gap of 2)
        while n > 0:
            right = right.next
            n -= 1

        # ── Step 2: Move both pointers until right hits None ─────────────
        # the gap stays fixed at n, so when right falls off the end,
        # left is sitting exactly at the node BEFORE the nth from end
        #
        # after loop:
        # dummy → 1 → 2 → 3 → 4 → 5 → None
        #                   ↑              ↑
        #                  left          right
        # left.next is node 4 — the one to remove
        while right:
            left = left.next
            right = right.next

        # ── Step 3: Delete the target node ───────────────────────────────
        # skip over left.next by pointing directly to left.next.next
        left.next = left.next.next

        # return dummy.next instead of head in case head itself was deleted
        return dummy.next

           
        