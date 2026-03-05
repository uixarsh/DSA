class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        last_smaller = float("-inf")
        cnt_curr = 0
        longest = 1

        for i in range(n):
            if nums[i] == last_smaller+1:
                cnt_curr +=1
            elif nums[i] != last_smaller:
                cnt_curr = 1
            longest = max(longest, cnt_curr)
            last_smaller = nums[i]
        
        return longest