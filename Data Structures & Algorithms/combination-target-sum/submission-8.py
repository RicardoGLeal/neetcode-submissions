class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, acum, comb):
            if acum == target:
                res.append(comb.copy())
                return

            if i >= len(nums) or acum > target:
                return

            for j in range(i, len(nums)):
                if acum + nums[j] > target:
                    return
                comb.append(nums[j])
                dfs(j, acum + nums[j], comb)
                comb.pop()
            
        dfs(0, 0, [])
        return res

            


                


