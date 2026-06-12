class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach: Dynamic Programming with O(1) space.
        # dp[i] = max money obtainable using houses 0..i
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        #   - dp[i-1]: skip house i, keep the best result up to i-1
        #   - dp[i-2] + nums[i]: rob house i, so house i-1 is off-limits,
        #     add its value to the best result up to i-2
        # Since dp[i] only depends on dp[i-1] and dp[i-2], we don't need
        # the full array — just two rolling variables.
        # prev1 tracks dp[i-1], prev2 tracks dp[i-2] (one step further back)

        if len(nums) == 0:
            return 0

        prev1, prev2 = 0, 0  # base case: "dp[-1]" and "dp[-2]" are both 0

        for num in nums:
            # curr = best result including the current house's decision
            curr = max(prev1, prev2 + num)  # skip vs. rob current house
            prev2 = prev1                   # shift window: dp[i-2] <- dp[i-1]
            prev1 = curr                    # shift window: dp[i-1] <- dp[i]

        # prev1 holds dp[n-1], the answer for the full array
        return prev1