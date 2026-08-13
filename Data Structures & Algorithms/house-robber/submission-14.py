class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+3)

        for i in range(n-1, -1, -1):
            dp[i] = max((nums[i] + dp[i + 2]), (nums[i] + dp[i + 3]))
        return max(dp[0], dp[1])