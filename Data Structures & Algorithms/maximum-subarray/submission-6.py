
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        greatest = nums[0]
        acum = 0

        for i in nums:
            if acum < 0:
                acum = 0
            acum += i
            greatest = max(acum, i, greatest)

        return greatest
 