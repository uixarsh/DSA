class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solve(nums, rslt, curr):
            
            if len(nums) == 0:
                rslt.append(curr[:])
                return

            ele = nums.pop(0)

            solve(nums, rslt, curr)
            curr.append(ele)
            solve(nums, rslt, curr)

            nums.insert(0, ele)
            curr.pop()

        rslt = []
        solve(nums, rslt, [])
        return rslt