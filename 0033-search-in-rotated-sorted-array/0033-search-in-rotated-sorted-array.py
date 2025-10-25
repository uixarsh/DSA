class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def findMinIdx ():
            start = 0
            end = (n-1)

            while start<=end:
                mid = start + (end-start)//2
                prev = (mid+n-1)%n
                nex = (mid+1)%n

                # If already sorted
                if nums[start] <= nums[end]:
                    return start

                if nums[mid] <= nums[prev] and nums[mid] <= nums[nex]:
                    return mid

                # Find the Unsorted Array now
                if nums[start] <= nums[mid]:
                    start = mid+1
                
                elif nums[mid] <= nums[end]:
                    end = mid-1

        def bs (start, end):
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return -1

        min_ele = findMinIdx()
        return max(bs(0,min_ele-1), bs(min_ele, (n-1)))
