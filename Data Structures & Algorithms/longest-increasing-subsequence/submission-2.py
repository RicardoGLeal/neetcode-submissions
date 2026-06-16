class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Suffix DP, filled right-to-left.
        # dp[i] = length of the longest strictly-increasing subsequence STARTING at i.
        # An element to the right (j) is attachable iff nums[j] > nums[i];
        # then the run "nums[i] + (best run starting at j)" has length 1 + dp[j].
        # Each dp[i] is the max over all valid j (or 1, just itself, if none qualify).
        # Answer is the best starting point anywhere, so max over the whole table.

        dp = [1] * len(nums)              # base case: every element is a length-1 run by itself

        for i in range(len(nums) - 1, -1, -1):       # right-to-left: every dp[j>i] is already final
            for j in range(i + 1, len(nums)):        # scan everything to i's right
                if nums[i] < nums[j]:                # j attachable? (strictly greater keeps it increasing)
                    dp[i] = max(dp[i], 1 + dp[j])     # accumulate: best candidate vs. best-so-far for this i

        return max(dp)                   # longest run can start at any index