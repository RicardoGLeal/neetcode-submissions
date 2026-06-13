class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def getMaxMoney(nums):
            if len(nums) == 0:
                return 0

            prev1, prev2 = 0, 0
            for i,num in enumerate(nums):
                curr = max(prev1, prev2 + num)
                prev1, prev2 = curr, prev1
            return prev1

        return max(getMaxMoney(nums[1:]), getMaxMoney(nums[:-1]))