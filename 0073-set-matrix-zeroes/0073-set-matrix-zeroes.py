class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_found = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Store the row number and column number
                    zero_found.append((i,j))

        for i, j in zero_found:
            # i -> row
            # j -> col
            x = y = 0

            while x<n:
                matrix[i][x] = 0
                x+=1

            while y<m:
                matrix[y][j] = 0
                y+=1