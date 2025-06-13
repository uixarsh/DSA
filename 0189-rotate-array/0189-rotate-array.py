class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        lst = [0]*N
        for i in range(N):
            pos = (i+k)%N
            lst[pos] = nums[i]
        
        nums[0:] = lst
