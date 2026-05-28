class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        def solve(nums, n, rslt, curr):
            if n == 0:
                rslt.append(curr[:])
                return

            for i in range(n):
                ele = nums[i]
                curr.append(ele)
                nums.pop(i)
                solve(nums, n-1, rslt, curr)
                nums.insert(i, ele)
                curr.pop()

        rslt = []
        solve(nums, len(nums), rslt, [])

        final = []
        for ele in rslt:
            if ele not in final:
                final.append(ele)
        return final