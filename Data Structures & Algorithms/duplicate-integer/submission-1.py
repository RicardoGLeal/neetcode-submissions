class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0
        numsSet = set() 
        for i in range(0, len(nums)):
            if nums[i] in numsSet:
                return True
            else: 
                numsSet.add(nums[i])
        return False