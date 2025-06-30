class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        m, n = len(matrix), len(matrix[0])
        hi = (m*n)-1

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            ro = mid//n
            col = mid%n
            if matrix[ro][col] == target:
                return True
            
            if matrix[ro][col] > target:
                hi = mid-1
            else:
                lo = mid+1

        return False