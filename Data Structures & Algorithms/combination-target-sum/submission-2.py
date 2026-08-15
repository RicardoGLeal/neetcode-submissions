class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        
        def dfs(acum, i):
            if i >= len(nums) or acum > target:
                return

            if acum == target:
                res.append(comb.copy())
                return
            
            if acum < target:
                comb.append(nums[i])
                dfs(acum + nums[i], i)
                comb.pop()
                dfs(acum, i + 1)
            
        for i in range(len(nums)):
            comb.append(nums[i])
            dfs(nums[i], i)
            comb.pop()

        return res

            


                


