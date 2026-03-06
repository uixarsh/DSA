class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # SUM
        # 1 to n2 ka sum
        # 1+2+3+4 = 10

        mpp = {}
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in mpp:
                    mpp[grid[i][j]] = 1
                else:
                    mpp[grid[i][j]] += 1

        rslt = [0, 0]
        n = n**2
        n_sum = (n)*(n+1) // 2
        found_sum = 0

        for k, v in mpp.items():
            if v==2:
                rslt[0] = k
            found_sum+=k

        rslt[1] = (n_sum-found_sum)
        return rslt

