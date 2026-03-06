class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # S1 = n²(n² + 1) / 2
        # actual_sum = S1 - b + a

        # S2 = n²(n²+1)(2n²+1)/6
        # actual_sq_sum = S2 - b² + a²

        n = len(grid)

        # Actual
        t = n**2
        actual_s1 = t*(t+1)//2
        actual_s2 = t*(t+1)*(2*t+1) // 6

        # Found
        found_s1 = 0
        found_s2 = 0

        for i in range(n):
            for j in range(n):
                ele = grid[i][j]
                found_s1 += ele
                found_s2 += (ele*ele)

        # (a-b) = found_s1 - actual_s1
        # (a² - b²) = (a-b)(a+b) = found_s2 - actual_s2
        # (a+b) = (found_s2 - actual_s2) / (a-b)

        x = found_s1 - actual_s1
        y = (found_s2 - actual_s2 ) // x

        a = (x+y) // 2
        b = a - x

        return [a, b]

        