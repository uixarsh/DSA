class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        slow_ptr=0
        fast_ptr=1
        N = len(nums)
        while fast_ptr <= (N-1):
            if nums[slow_ptr] == nums[fast_ptr]:
                return nums[slow_ptr]
            slow_ptr+=1
            fast_ptr+=1
        return -1