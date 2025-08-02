class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(nums, k):
            l = 0
            res = 0
            n = len(nums)
            odd_count = 0
            for r in range(n):
                if nums[r] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2 == 1:
                        odd_count -= 1
                    l += 1
                # For each position of r, there are (r-l+1) valid subarrays ending at r
                res += (r - l + 1)
            return res
        return atMost(nums, k) - atMost(nums, k-1)