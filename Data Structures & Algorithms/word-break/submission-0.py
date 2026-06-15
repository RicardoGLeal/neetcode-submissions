class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom-up DP over suffixes.
        # dp[i] = True iff s[i:] can be segmented into dictionary words.
        # Recurrence: dp[i] is True if some word w fits at i AND dp[i+len(w)] is True.
        # Fill right-to-left so dp[i+len(w)] is already known when we read it.
        # Complexity:
        #   Time:  O(n * m * k) where n = len(s), m = len(wordDict),
        #          k = avg word length (the substring slice + equality check).
        #   Space: O(n) for the dp array.

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True                                  # empty suffix is breakable

        for i in range(len(s) - 1, -1, -1):                # right-to-left
            for w in wordDict:                             # try each word as the first piece
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]                 # breakable iff remainder is

                # Early exit: once dp[i] is True, no need to test more words
                # — one valid segmentation is all we need for this position.
                if dp[i]:                                  
                    break

        return dp[0]                                       # whole string = suffix from 0