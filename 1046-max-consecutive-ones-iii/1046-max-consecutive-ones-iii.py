class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l_ptr = 0
        r_ptr = 0
        n = len(nums)
        max_len = 0
        curr_sum = 0
        while r_ptr < n:
            curr_sum+=nums[r_ptr]
            if (r_ptr - l_ptr + 1) - curr_sum > k:
                curr_sum-=nums[l_ptr]
                l_ptr+=1
            max_len = max(max_len, (r_ptr - l_ptr + 1))
            r_ptr+=1

        return max_len