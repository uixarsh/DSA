class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        # Function to find the index of the smallest value (pivot point)
        def find_pivot(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        # Standard binary search
        def binary_search(left, right, nums, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        pivot = find_pivot(nums)
        n = len(nums)

        if pivot == 0:
            # The array is not rotated
            return binary_search(0, n - 1, nums, target)
        if nums[0] <= target <= nums[pivot - 1]:
            # Target lies in the left sorted portion
            return binary_search(0, pivot - 1, nums, target)
        else:
            # Target lies in the right sorted portion
            return binary_search(pivot, n - 1, nums, target)