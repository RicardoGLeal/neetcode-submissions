from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            elif tails[i] >= x:
                tails[i] = x
            else:
                tails.append(x)
        return len(tails) 

        # nums = [9,1,4,2,3,3,7]

        # [9]
        # [1]
        # [1, 4]
        # [1, 2]
        # [1, 2, 3]
        # [1, 2, 3]

