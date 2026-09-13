class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0
            
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            ways = dfs(i+1, currSum+nums[i]) + dfs(i+1, currSum-nums[i])
            memo[(i, currSum)] = ways
            return ways
            
        return dfs(0, 0)
            




        

