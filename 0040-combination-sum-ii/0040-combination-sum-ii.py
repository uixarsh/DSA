class Solution:
    def combinationSum2(self, candidates: List[int], target: int):

        candidates.sort()
        n = len(candidates)

        def solve(idx, summ, curr):

            if summ == target:
                rslt.append(curr[:])
                return True

            if idx >= n or summ > target:
                return False
            
            ele = candidates[idx]
            
            if ele > target - summ:
                return

            # NOT PICK
            next_idx = idx + 1
            while next_idx < n and candidates[next_idx] == ele:
                next_idx += 1

            solve(next_idx, summ, curr)

            # PICK
            curr.append(ele)
            solve(idx + 1, summ + ele, curr)
            curr.pop()

        rslt = []
        solve(0, 0, [])
        return rslt