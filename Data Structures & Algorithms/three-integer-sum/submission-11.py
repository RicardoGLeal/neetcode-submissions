class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i, v in enumerate(nums):

            if v > 0:
                continue

            if i > 0 and v == nums[i-1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                if v + nums[l] + nums[r] > 0:
                    r -= 1
                    continue

                elif v + nums[l] + nums[r] < 0:
                    l += 1 
                    continue

                res.append([v,nums[l], nums[r]])

                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1 
        return res