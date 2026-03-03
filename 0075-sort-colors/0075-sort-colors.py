class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Detuch National flag Algorithm
        """
        n = len(nums)
        low = 0
        # Say whole array contains in region (mid, high) i.e, unsorted one
        mid = 0
        high = (n-1)

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
            
