class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(idx, summ ,curr, rslt):
            if idx == n:
                return

            if summ > target:
                return

            if summ == target:
                rslt.append(curr[:])
                return

            ele = candidates[idx] 
            curr.append(ele)
            solve(idx, summ+ele, curr, rslt)
            curr.pop()

            solve(idx+1, summ, curr, rslt)

        n = len(candidates)
        rslt = []
        solve(0, 0, [], rslt)
        return rslt