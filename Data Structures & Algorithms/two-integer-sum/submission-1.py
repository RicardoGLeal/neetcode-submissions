class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {} # val -> index
        for i in range(0, len(nums)):
            neededNum = target-nums[i]
            if neededNum in numsMap:
                return [numsMap[neededNum], i]
            numsMap[nums[i]] = i