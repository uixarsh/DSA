class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary Search
        # Search First index as well as Last Index 
        # O(log n)
        return [self.binary_srch(nums, target, False), self.binary_srch(nums, target, True)]
        

    def binary_srch(self, nums, target, findFirstIdx):
        first = 0
        last = len(nums)-1
        res = -1
        while first <= last:
            mid = first + (last-first)//2
            if nums[mid] > target:
                last = mid-1
            elif nums[mid] < target:
                first = mid+1
            else:
                res = mid
                if findFirstIdx:
                    first = mid+1       # Checking for last occurence
                else:
                    last = mid-1         # Checking for first occurence
        return res