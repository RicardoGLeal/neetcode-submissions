class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev1, prev2 = 0, 0

        for idx, num in enumerate(nums):
            if idx == 0:
                prev1 = nums[0]
            else:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
                
        return prev1