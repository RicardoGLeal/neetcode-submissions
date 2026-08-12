class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        acum = 1

        for i in range(1, n):
            acum *= nums[i-1]
            res[i] = acum
        
        acum = 1
        for i in range(n-2, -1, -1):
            acum *= nums[i+1]
            res[i] *= acum
        return res

        
        