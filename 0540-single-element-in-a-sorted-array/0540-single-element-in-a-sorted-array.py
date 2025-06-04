class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # Check for single element in List
        if n==1:
            return nums[0]
        # Check for left most element
        if nums[0] != nums[1]:
            return nums[0]
        # Check for right most element
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        start = 1
        end = len(nums) - 2
        while start <= end:
            mid = start + (end-start)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            # Checking for left side of single element:
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                start = mid+1
            else:
                end = mid-1
        return -1
