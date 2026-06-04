class Solution:
    def combinationSum2(self, candidates: List[int], target: int):

        candidates.sort()
        n = len(candidates)

        def solve(idx, summ, curr):

            if summ == target:
                rslt.append(curr[:])
                return

            if idx >= n or summ > target:
                return

            # NOT PICK
            next_idx = idx + 1
            while next_idx < n and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            solve(next_idx, summ, curr)

            # PICK
            curr.append(candidates[idx])
            solve(idx + 1, summ + candidates[idx], curr)
            curr.pop()

        rslt = []
        solve(0, 0, [])
        return rslt