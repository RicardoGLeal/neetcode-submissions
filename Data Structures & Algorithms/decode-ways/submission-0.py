class Solution:
    def numDecodings(self, s: str) -> int:
        # APPROACH: Top-down recursion with memoization.
        #
        # Define f(i) = number of ways to decode the suffix s[i:].
        # At each position we have at most two choices:
        #   (1) decode s[i] as a single letter (1-9), then solve f(i+1)
        #   (2) decode s[i:i+2] as a two-letter code (10-26), then solve f(i+2)
        # The answer for position i is the SUM of the ways from each legal choice,
        # because every valid decoding takes exactly one of these moves first.
        #
        # Two gates make this harder than plain Climbing Stairs:
        #   - a leading '0' is never a valid single decode (no letter maps to 0)
        #   - the two-digit move is only legal when s[i:i+2] is in [10, 26]
        #
        # Different decoding paths converge on the same suffix (overlapping
        # subproblems), so memo[i] caches each index's answer to avoid
        # recomputing it. This turns O(2^n) into O(n) time, O(n) space.

        n = len(s)
        memo = {}

        def f(i):
            # Base case: we've consumed the entire string. An empty suffix
            # has exactly one decoding (the empty decoding), so return 1.
            if i == n:
                return 1

            # A '0' here can't start any valid decode: no single letter is 0,
            # and we only reach this index as the START of a decode, so '0X'
            # was never an option. This path is dead — return 0.
            # (Note: this sits ABOVE the memo write, so a '0' index is never
            # cached. That's fine — it always returns 0 in O(1) anyway.)
            if s[i] == '0':
                return 0

            # If we've already solved this suffix, reuse the stored answer
            # instead of re-walking the whole subtree below it.
            if i in memo:
                return memo[i]

            # Choice 1 (always legal here, since s[i] != '0'):
            # take s[i] as a single digit and decode the rest.
            ways = f(i + 1)

            # Choice 2: take s[i:i+2] as a two-digit code, but only if
            #   - there are two characters left (i + 1 < n), AND
            #   - the value is in [10, 26]: either s[i] == '1' (10-19, any
            #     second digit), or s[i] == '2' with second digit 0-6 (20-26).
            # The (i + 1 < n) guard wraps BOTH inner checks so s[i+1] is never
            # accessed out of bounds.
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                ways += f(i + 2)

            # Cache and return this index's total before unwinding.
            memo[i] = ways
            return ways

        return f(0)