class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt+=1
                max_ones = max(max_ones, cnt)
            if i == 0:
                cnt = 0

        return max_ones