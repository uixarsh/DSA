class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def solve(idx, curr):

            if idx == n:
                rslt.append(curr[:])
                return

            nxt = idx + 1
            while nxt < n and nums[nxt] == nums[idx]:
                nxt += 1
            
            # Unpick
            solve(nxt, curr)

            # Pick 
            curr.append(nums[idx])
            solve(idx+1, curr)
            curr.pop()

        n = len(nums)
        rslt = []
        solve(0, [])
        return rslt