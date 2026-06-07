# Approach: backtracking with a for loop over remaining candidates.
# At each call we try every candidate from index `start` onward,
# appending it to curr and recursing with a reduced remaining. Passing
# i allows reuse of the same element. We sort first so we
# can break early the moment a candidate exceeds remaining.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # sort so we can break early when c > remaining

        def dfs(start, curr, remaining):
            if remaining == 0:
                res.append(curr[:])  # snapshot curr — don't store the live reference
                return               # stop exploring; can't improve on an exact match

            for i in range(start, len(nums)):
                c = nums[i]

                if c > remaining:
                    break  # sorted → all subsequent candidates also too large

                curr.append(c)               # choose: add candidate to current combo
                dfs(i, curr, remaining - c)  # explore: i (not i+1) allows reuse of same element
                curr.pop()                   # undo: backtrack before trying next candidate

        dfs(0, [], target)
        return res