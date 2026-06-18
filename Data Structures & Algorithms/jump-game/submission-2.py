
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0 

        for i,num in enumerate(nums):
            if i <= reach:
                candReach = i+num
                reach = max(reach, candReach)
        if reach >= len(nums)-1:
            return True
        return False
        
            

