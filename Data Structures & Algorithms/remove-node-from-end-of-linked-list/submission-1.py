# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = head
        length = 0

        while aux:
            length += 1
            aux = aux.next
        
        index = length - n
        if index == 0:
            return head.next            

        counter = -1
        aux = head
        while aux:
            counter += 1
            if (counter + 1 == index):
                aux.next = aux.next.next 
                return head
            aux = aux.next
        return head            
        