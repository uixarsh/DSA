class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Brute: O(N^2), counter and subarrays
        Better: Map and check
        Optimal : XOR Gate
        '''
        n = len(nums)
        ans = nums[0]
        for i in range(1, n):
            ans^=nums[i]
        
        return ans