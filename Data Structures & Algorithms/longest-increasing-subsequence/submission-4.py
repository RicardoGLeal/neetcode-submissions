from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # IDEA: build the longest increasing run by keeping a list called `tails`.
        # tails[k] = the smallest number that an increasing run of length (k+1) can end with.
        # Why smallest? A run ending in a small number is easier to extend later,
        # because more future numbers will be bigger than it.
        # tails always stays sorted, so we can find where each number fits with binary search.
        # At the end, the LENGTH of tails is the answer (not its contents).

        tails = []
        for x in nums:
            # Find the first spot in tails holding a number >= x.
            i = bisect_left(tails, x)

            if i == len(tails):
                # x is bigger than everything in tails:
                # it extends the longest run we have, so the answer grows by 1.
                tails.append(x)
            else:
                # x replaces a bigger number, making that run end in something smaller.
                # Same length run, but now easier to extend in the future.
                tails[i] = x

        # Length of tails = length of the longest increasing subsequence.
        return len(tails)


        # nums = [9,1,4,2,3,3,7]

        # [9]
        # [1]
        # [1, 4]
        # [1, 2]
        # [1, 2, 3]
        # [1, 2, 3]

