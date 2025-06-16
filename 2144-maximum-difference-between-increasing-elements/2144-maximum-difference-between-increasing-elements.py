class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        diff = -1
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    curr_diff = nums[j] - nums[i]
                    if curr_diff > diff:
                        diff = curr_diff
        
        return diff
