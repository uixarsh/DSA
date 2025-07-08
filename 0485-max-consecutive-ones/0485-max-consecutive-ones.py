class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        n = len(nums)
        for i in range (n):
            if nums[i] == 0:
                curr_len = 0
                continue
            curr_len += 1
            max_len = max(curr_len, max_len)
        return max_len