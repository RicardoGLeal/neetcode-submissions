class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def getMaxMoney(start, end):
            if len(nums) == 0:
                return 0

            prev1, prev2 = 0, 0
            for i in range(start, end):
                curr = max(prev1, prev2 + nums[i])
                prev1, prev2 = curr, prev1
            return prev1

        return max(getMaxMoney(1, len(nums)), getMaxMoney(0, len(nums)-1))