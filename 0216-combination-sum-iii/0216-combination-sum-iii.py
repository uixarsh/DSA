class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        if k>n:
            return []

        def solve(k, curr, n, rslt, prev_sum, pair):           
            if not k:
                if prev_sum == n:
                    rslt.append(pair[:])
                return
            
            for i in range(curr, 10):
                curr_sum = i + prev_sum
                pair.append(i)
                solve (k-1, i+1, n, rslt, curr_sum, pair)
                pair.pop()

        rslt = []
        solve(k, 1,  n, rslt, 0, [])
        return rslt