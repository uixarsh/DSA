class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        start_ptr = 0
        next_ptr = 1
        N = len(nums)
        diffr = []
        while start_ptr < next_ptr and next_ptr < N:
            while next_ptr < N:
                if nums[start_ptr] < nums[next_ptr]:
                    diffr.append(nums[next_ptr] - nums[start_ptr])
                next_ptr+=1
            start_ptr+=1
            next_ptr = start_ptr+1
            
        
        return max(diffr) if diffr else -1
