class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def solve(i):
            if i == len(nums):
                rslt.append(curr[:])
                return

            solve(i + 1)

            curr.append(nums[i])
            solve(i + 1)
            curr.pop()

        rslt = []
        curr = []
        solve(0)
        return rslt