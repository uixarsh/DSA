class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 1
        j = (n-i-1)
        l_sum = [0]*n
        r_sum = [0]*n
        rslt = [0]*n

        while i < n and j >= 0:
            l_sum[i] = nums[i-1] + l_sum[i-1]
            r_sum[j] = nums[j+1] + r_sum[j+1]
            i+=1
            j-=1

        for i in range(n):
            rslt[i] = abs(l_sum[i] - r_sum[i])

        return rslt