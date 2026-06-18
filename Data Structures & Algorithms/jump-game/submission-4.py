
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0 

        for i,num in enumerate(nums):
            if i <= reach:
                reach = max(reach, i+num)
            else:
                return False
        return True