class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        prev1, prev2 = 0, 0

        for i in range(n-1, -1, -1):
            prev1, prev2 = max(prev1, nums[i] + prev2), prev1
        return prev1