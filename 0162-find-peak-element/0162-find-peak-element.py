class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return (n-1)
        
        start = 1
        end = n-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            # Element are increasing in order
            elif nums[mid-1] < nums[mid]:
                start = mid+1
            
            # Elements are decreasing in order
            # 
            else:
                end = mid-1

        return -1