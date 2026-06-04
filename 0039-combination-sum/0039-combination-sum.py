class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # HYPOTHESIS : Either Consider the same element or increase the index
        def solve(idx, summ ,curr):

            if summ == target:
                rslt.append(curr[:])
                return

            if summ > target:
                return

            if idx >= n:
                return

            ele = candidates[idx] 
            curr.append(ele)
            solve(idx, summ+ele, curr)
            curr.pop()

            solve(idx+1, summ, curr)

        n = len(candidates)
        rslt = []
        solve(0, 0, [])
        return rslt