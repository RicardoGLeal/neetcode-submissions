class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i,currNums, acum):
            if acum == target:
                res.append(currNums.copy())
                return
                
            if i >= len(nums) or acum > target:
                return

            for j in range(i, len(nums)):
                if acum + nums[j] <= target:
                    currNums.append(nums[j])
                    dfs(j, currNums, acum + nums[j])
                    currNums.pop()
                else:
                    return 

        dfs(0,[],0)
        return res
            
