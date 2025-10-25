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
            # else:
                end = mid-1

        return -1



# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start = 0
#         end = len(nums) - 1

#         while start <= end:
#             # If the subarray is already sorted
#             if nums[start] <= nums[end]:
#                 return nums[start]

#             mid = start + (end - start) // 2

#             # Check if mid is the minimum
#             if nums[mid] < nums[mid - 1]:
#                 return nums[mid]
#             if nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]

#             if nums[start] <= nums[mid]:
#                 start=mid+1
#             else:
#                 end=mid-1