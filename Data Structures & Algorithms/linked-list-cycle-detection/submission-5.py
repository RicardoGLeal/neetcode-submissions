# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next        # move 1 step
            fast = fast.next.next   # move 2 steps

            if slow is fast:        # pointers met → cycle exists
                return True

        # fast hit None → list has a tail, no cycle
        return False
        