class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        diff = -1
        premin = nums[0]

        for i in range(N):
                if nums[i] > premin:
                    diff = max(diff, nums[i] - premin)
                else:
                    premin = nums[i]
        return diff
