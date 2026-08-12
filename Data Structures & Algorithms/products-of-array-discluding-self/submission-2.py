class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        acum = 1

        for i in range(n):
            res[i] = acum
            acum *= nums[i]
        
        acum = 1
        for i in range(n-1, -1, -1):
            res[i] *= acum
            acum *= nums[i]
        return res

        
        