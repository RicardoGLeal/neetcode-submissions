class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Modified Kadane's: track both max AND min product ending at each index, because
        # a negative num can flip the previous min into the new max (neg * neg = big pos).
        # At each step, best/worst ending here is one of: num alone, num*prevMax, num*prevMin.
        # Time: O(n), Space: O(1).

        curMax, curMin = 1, 1   # max/min product ending at previous index (1 = identity)
        res = nums[0]           # not 0 — handles all-negative arrays like [-5]

        for num in nums:
            curMax, curMin = (
                max(num, curMax * num, curMin * num),
                min(num, curMin * num, curMax * num),
            )
            res = max(res, curMax)  # best subarray can end at any index, not just the last

        return res

                


        