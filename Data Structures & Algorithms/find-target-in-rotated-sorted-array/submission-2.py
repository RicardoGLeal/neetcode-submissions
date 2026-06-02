class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        # --- Pass 1: Find the pivot (index of the smallest element) ---
        while l < r: 
            mid = (l + r) // 2

            # If mid element is greater than rightmost, the pivot must be in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, pivot is in the left half (mid could be the pivot itself)
            else:
                r = mid
        
        pivot = l  # pivot is the index of the smallest element (start of the original array)

        # --- Pass 2: Determine which half to binary search ---
        if pivot == 0:
            # Array is not rotated, search the entire array
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[pivot - 1]:
            # Target lies in the left sorted portion (before the rotation point)
            l, r = 0, pivot - 1
        else:
            # Target lies in the right sorted portion (after the rotation point)
            l, r = pivot, len(nums) - 1

        # --- Pass 3: Standard binary search on the chosen half ---
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid  # Target found, return its index
        
        return -1  # Target not in array

