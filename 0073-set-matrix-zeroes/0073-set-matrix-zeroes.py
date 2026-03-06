class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Detect if first row originally has a zero
        for col in range(n):
            if matrix[0][col] == 0:
                first_row_zero = True
        
        # Detect if first column originally has a zero
        for row in range(m):
            if matrix[row][0] == 0:
                first_col_zero = True

        # Mark the First Row and Fist Column Elements as Zero
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0  # col marker
                    matrix[row][0] = 0  # row marker

        # Business logic
        # Make the remaining matrix elements as zero starting from (1,1)
        # take help of marking on first row and first col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # Now check those first row does it contain any zero
        if first_row_zero:
            for col in range(n):
                matrix[0][col] = 0

        # check first col does it contain any zero
        if first_col_zero:
            for row in range(m):
                matrix[row][0] = 0