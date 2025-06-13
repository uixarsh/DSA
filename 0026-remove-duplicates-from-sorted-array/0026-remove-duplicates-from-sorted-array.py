class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start_ptr = 0
        move_ptr = 1
        N = len(nums)
        while move_ptr < N:
            if nums[start_ptr] != nums[move_ptr]:
                start_ptr+=1
                nums[start_ptr] = nums[move_ptr]
            move_ptr+=1
        return start_ptr+1