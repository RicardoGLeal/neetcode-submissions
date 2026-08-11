class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range (1, n + 1):
            base = res[i >> 1]
            res[i] = base + (i & 1)
        return res
        