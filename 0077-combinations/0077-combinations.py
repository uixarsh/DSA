class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if n<k:
            return []
        
        def solve(n, k, curr, rslt, tmp):
            if k==0:
                rslt.append(tmp[:])
                return

            for i in range(curr, n+1):
                tmp.append(i)
                solve(n, k-1, i+1, rslt, tmp)
                tmp.pop()

        rslt = []
        solve(n, k, 1, rslt, [])
        return rslt