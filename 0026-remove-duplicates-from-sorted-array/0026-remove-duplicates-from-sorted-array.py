class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 POINTER APPROACH
        i = 0
        j = (i+1)
        n = len(nums)

        while j<n:
            if nums[j] > nums[i]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
        
        del nums[i+1:j]