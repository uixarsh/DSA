class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return n-1

        start = 1
        end = (n-2)

        while start <= end:
            mid = start + (end-start)//2
            next_idx = mid+1
            prev_idx = mid-1

            if nums[mid] > nums[next_idx] and nums[mid] > nums[prev_idx]:
                return mid
            
            if nums[mid] > nums[prev_idx]:
                start = mid+1
            else:
                end = mid-1

        return -1