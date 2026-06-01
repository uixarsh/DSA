class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        def solve(nums, n, rslt, curr):
            if n == 0:
                rslt.append(curr[:])
                return
            
            for i in range(n):

                if i > 0 and nums[i] - nums[i-1] == 0:
                    continue
                
                ele = nums.pop(i)
                curr.append(ele)
                
                solve(nums, n-1, rslt, curr)

                nums.insert(i, ele)
                curr.pop()
        
        rslt = []
        solve(nums, len(nums), rslt, [])
        return rslt