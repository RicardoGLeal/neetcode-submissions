# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy node acts as a placeholder so every real node
        # is attached identically — no special case for the head
        dummy = ListNode(-1)
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        # Attach the remaining tail (one of these is None)
        prev.next = list1 if list1 else list2

        # dummy.next is the true head of the merged list
        return dummy.next
