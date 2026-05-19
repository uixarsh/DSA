class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def bs(nums : List[int], ele : int):
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == ele:
                    return mid
                elif nums[mid] > ele:
                    end = mid-1
                else:
                    start = mid+1
            return None

        for ele in nums1:
            x = bs(nums2, ele)
            if x is not None:
                return ele
        return -1