
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        greatest = nums[0]
        acum = nums[0]

        for i in range(1, len(nums)):
            if acum < 0:
                acum = 0
            acum += nums[i]
            greatest = max(acum, greatest)

        return greatest
 