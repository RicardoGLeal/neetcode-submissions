class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(l):
            if l >= len(s):
                res.append(part.copy())
                return

            for r in range(l, len(s)):
                if self.isPali(s, l, r):
                    part.append(s[l : r + 1]) 
                    dfs(r + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        