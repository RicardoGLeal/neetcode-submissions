class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isFeasible(cap):
            curSum = 0
            pieces = 1 
            
            for num in nums:
                if curSum + num > cap:
                    pieces += 1
                    curSum = num
                    if pieces > k:
                        return False
                else:
                    curSum += num
            return True

                
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            if isFeasible(mid):
                high = mid
            else:
                low = mid + 1
        return low 


        


        