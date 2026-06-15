class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                remaining = amount - coin

                if remaining >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            memo[amount] = res
            return res
            
        res = dfs(amount)
        if res >= 1e9:
            return -1
        return res
        