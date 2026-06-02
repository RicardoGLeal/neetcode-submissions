class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:  # stop when pointers meet (found the minimum)
            mid = left + (right - left) // 2  # avoids overflow, midpoint of current window

            if nums[mid] > nums[right]:
                # mid is in the LEFT (larger) part of the rotation
                # minimum must be somewhere to the RIGHT of mid
                left = mid + 1
            else:
                # mid is in the RIGHT (smaller) part of the rotation
                # minimum is at mid or somewhere to the LEFT of mid
                right = mid  # don't do mid-1, mid itself could be the minimum

        # left == right, both pointers converged on the minimum
        return nums[left]
                    
