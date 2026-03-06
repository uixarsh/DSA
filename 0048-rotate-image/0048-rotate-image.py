class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = n = len(matrix)

        # Take Transpose of the Matrix
        for row in range(m):
            for col in range(n):
                if col > row:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Revese the Rows
        for ele in matrix:
            ele.reverse()
