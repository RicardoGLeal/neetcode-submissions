class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 1

        for i in range(n-1, 0, -1):
            temp = prev1
            prev1 = prev1 + prev2
            prev2 = temp
        return prev1