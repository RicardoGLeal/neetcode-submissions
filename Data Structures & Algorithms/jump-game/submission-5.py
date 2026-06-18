# Jump Game (greedy)
#
# Goal: nums[i] is the MAX jump length from index i. Start at index 0.
# Return True if you can reach the last index.
#
# Key idea: don't enumerate jump combinations. Track one number as you scan
# left to right:
#   reach = the farthest index reachable so far, given everything seen
#
# At each index i, two steps in order:
#   1. Stranded check: if i > reach, no path can even stand on i (and so none
#      can pass it) -> return False. This is a hard stop, not a skip.
#   2. Update: from i you can land as far as i + nums[i] (an absolute index,
#      not a running total), so reach = max(reach, i + nums[i]).
#
# Why one number captures all paths: reach already IS the best any sequence of
# jumps could achieve so far. Reachability propagates through the i <= reach
# permission check, not by summing jump lengths.
#
# If the loop finishes without ever stranding, every index was reachable -
# including the last -> True.
#
# Time: O(n)   Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0                          # farthest index reachable so far

        for i, num in enumerate(nums):
            if i > reach:                  # can't reach i, so can't reach anything past it
                return False
            reach = max(reach, i + num)    # i + num = farthest absolute index from here

        return True                        # never stranded => last index was reachable