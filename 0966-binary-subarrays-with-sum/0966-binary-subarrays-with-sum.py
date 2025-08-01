class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def solve(nums, goal):
            # Determines all the subarrays with sum <= goal
            if goal < 0:
                return 0

            l=0
            r=0
            curr_sum=0
            n=len(nums)
            cnt=0

            while r<n:
                curr_sum+=nums[r]
                while curr_sum > goal:
                    curr_sum-=nums[l]
                    l+=1
                cnt+=(r-l+1)
                r+=1

            return cnt

        return solve(nums,goal) - solve(nums, (goal-1))  # (subarray sum <=k) - (subarray sum <= (k-1)) = subarray sum == k