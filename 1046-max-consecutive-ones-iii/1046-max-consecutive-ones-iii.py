class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        max_len = 0
        curr_len = 0
        while r < n:
            curr_len += nums[r]
            if ((r-l+1) - curr_len) > k:
                curr_len -= nums[l]
                l+=1

            max_len = max(max_len, (r-l+1))
            r+=1

        return max_len