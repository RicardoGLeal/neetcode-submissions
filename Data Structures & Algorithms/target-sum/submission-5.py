class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # (i, currSum) -> number of ways to finish from this state

        def dfs(i, currSum):
            if i == len(nums):                    # base case: all signs assigned
                return 1 if currSum == target else 0

            if (i, currSum) in memo:              # seen this state before? reuse it
                return memo[(i, currSum)]

            # try +nums[i] and -nums[i], sum up ways from both branches
            ways = dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
            memo[(i, currSum)] = ways             # cache before returning
            return ways

        return dfs(0, 0)
                




        

