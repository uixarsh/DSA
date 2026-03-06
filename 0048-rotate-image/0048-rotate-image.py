class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = n = len(matrix)

        rslt = []

        for col in range(n):
            temp = []
            for row in range(n-1, -1, -1):
                temp.append(matrix[row][col])

            rslt.append(temp)

        matrix[:] = rslt[:]
                