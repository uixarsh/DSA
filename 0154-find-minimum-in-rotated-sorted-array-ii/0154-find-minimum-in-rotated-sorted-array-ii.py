class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = (n-1)
        
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                # min is in right half
                start = mid + 1
            elif nums[mid] < nums[end]:
                # min is at mid or in left half (including mid)
                end = mid
            else:  # nums[mid] == nums[end]
                # duplicates: shrink end safely
                end -= 1

        return nums[start]