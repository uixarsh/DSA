class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = (n-1)

        while start<=end:
            mid = start + (end-start)//2
            prev = (mid+n-1)%n
            nex = (mid+1)%n

            # If already sorted
            if nums[start] <= nums[end]:
                return nums[start]

            if nums[mid] <= nums[prev] and nums[mid] <= nums[nex]:
                return nums[mid]

            # Find the Unsorted Array now
            if nums[start] <= nums[mid]:
                start = mid+1
            
            elif nums[mid] <= nums[end]:
                end = mid-1

        return -1
