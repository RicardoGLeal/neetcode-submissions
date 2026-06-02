# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = l1

        if not l1 and not l2:
            return None
        
        if not l1:
            return l2
        
        if not l2:
            return l1

        if l1.val <= l2.val:
            prev = l1
            l1 = l1.next
        else:
            prev = l2
            l2 = l2.next
        head = prev

        while l1 and l2: 
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2

        return head
        
