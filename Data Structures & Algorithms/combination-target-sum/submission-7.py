class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, acum, comb):
            if i >= len(nums) or acum > target:
                return

            if acum == target:
                res.append(comb.copy())
                return
            
            if acum + nums[i] > target:
                dfs(i + 1, acum, comb)
                return

            comb.append(nums[i])
            dfs(i, acum + nums[i], comb)
            comb.pop()
            dfs(i + 1, acum, comb)
            
        dfs(0, 0, [])
        return res

            


                


