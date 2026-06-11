class Solution:
    def climbStairs(self, n: int) -> int:
        combinations = {}

        def dfs(num):
            if num in combinations: 
                return combinations[num]

            if num >= n:
                return num == n

            combinations[num] = dfs(num+1) + dfs(num+2)
            return combinations[num]

        return dfs(0)
        

