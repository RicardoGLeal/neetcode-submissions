# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            # ── Step 1: Find the middle ───────────────────────────────────────
            # slow moves 1 step, fast moves 2 steps
            # when fast reaches the end, slow is at the midpoint
            slow, fast = head, head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # ── Step 2: Sever the list into two halves ────────────────────────
            # Example: 1 → 2 → 3 → 4 → 5
            #                    ↑
            #                   slow (midpoint)
            #
            # second: 4 → 5
            # first:  1 → 2 → 3 → None  (slow.next = None cuts the link)
            second = slow.next
            slow.next = None

            # ── Step 3: Reverse the second half ──────────────────────────────
            # 4 → 5 → None  becomes  5 → 4 → None
            #
            # We save next_node before overwriting curr.next,
            # since once we reverse the pointer we lose access to the rest of the list
            prev, curr = None, second

            while curr:
                next_node = curr.next  # save before overwriting
                curr.next = prev       # reverse the pointer
                prev = curr            # advance prev
                curr = next_node       # advance curr

            # prev is now the head of the reversed second half

            # ── Step 4: Merge the two halves ─────────────────────────────────
            # Interleave nodes from each half one at a time:
            #
            # l1:  1 → 2 → 3
            # l2:  5 → 4
            #
            # step 1: 1 → 5 → 2 → 3,  l2: 4
            # step 2: 1 → 5 → 2 → 4 → 3
            #
            # l2 drives the loop — second half is always equal or shorter,
            # so when l2 is exhausted, l1 sits on the middle node
            # which is already correctly placed at the end
            l1, l2 = head, prev

            while l1 and l2:
                l1_next = l1.next  # save next pointers before
                l2_next = l2.next  # overwriting them below

                l1.next = l2       # insert l2 node right after l1
                l2.next = l1_next  # connect l2 to the rest of l1

                l1 = l1_next       # advance both pointers
                l2 = l2_next

