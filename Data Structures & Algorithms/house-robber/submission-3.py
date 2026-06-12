class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAcum = [0] * len(nums)

        for idx, num in enumerate(nums):
            if idx == 0:
                maxAcum[0] = num
            elif idx == 1:
                maxAcum[1] = max(nums[0], num)
            else:
                maxAcum[idx] = max(maxAcum[idx-1], maxAcum[idx-2] + num)
        return max(maxAcum)

                
        