class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solve(nums, rslt, temp):
            if len(nums) == 0:
                rslt.append(temp)
                return

            op1 = temp.copy()
            op2 = temp.copy()
            op2.append(nums[0])
            nums = nums[1:]

            solve(nums, rslt, op1)
            solve(nums, rslt, op2)
            
        ans = []
        solve(nums, ans, [])

        return ans