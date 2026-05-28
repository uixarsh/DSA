class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def solve(arr, tgt, rslt, prev_sum, pair):

            if prev_sum == tgt:
                rslt.append(pair[:])
                return

            for ele in arr:
                curr_sum = prev_sum + ele
                if curr_sum > tgt:
                    break
                pair.append(ele)
                solve(arr, tgt, rslt, curr_sum, pair)
                pair.pop()

        rslt = []
        solve(candidates, target, rslt, 0, [])

        for ele in rslt:
            ele.sort()

        final = []

        for ele in rslt:
            if ele not in final:
                final.append(ele)

        return final