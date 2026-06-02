class Solution:
    def minWindow(self, s: str, t: str) -> str:
        neededMap = Counter(t)
        windowMap = {}

        needed = len(neededMap)
        have = 0

        l = 0
        res = [-1,-1]
        resLen = float("infinity")

        for r in range(len(s)):
            c = s[r]
            windowMap[c] = windowMap.get(c, 0) + 1
            if c in neededMap and neededMap[c] == windowMap[c]:
                have += 1
            
            while needed == have:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                c = s[l]
                windowMap[c] -= 1
                if c in neededMap and neededMap[c] > windowMap[c]: 
                    have -= 1
                l += 1 
        l, r = res
        if resLen != float("infinity"):
            return s[l : r+1]
        else:
            return ""
                
                
                

            



            
