# Maximum Subarray (Kadane's algorithm)
#
# Goal: find the largest sum of any contiguous subarray (at least one element).
#
# Key idea: every subarray ends somewhere. So ask, for each index i:
# "what's the best subarray sum ending exactly at i?" The overall answer is
# the best of those across all i.
#
# A subarray ending at i is either just nums[i] alone, or the best run ending
# at i-1 extended by nums[i]. Extending only helps when that prior run is
# positive; otherwise start fresh. That's the whole decision.
#
# We only ever need the previous index's best, so it collapses to two vars:
#   cur  = best subarray sum ending at the current index
#   best = best sum seen anywhere so far (the answer)
#
# Time: O(n)   Space: O(1)
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]              # base case: subarray ending at index 0 is nums[0]
 
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])   # start fresh, or extend the prior run
            best = max(best, cur)               # answer can live at any index, so track it each step
        return best
 