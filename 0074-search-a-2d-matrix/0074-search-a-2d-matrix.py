class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][len(matrix[i])-1] >=target:
                return self.BS(matrix[i], target)
        return False

    def BS(self,mat, tgt):
        lo = 0
        hi = len(mat)-1

        while lo<=hi:
            mid = lo + (hi-lo)//2

            if mat[mid] == tgt:
                return True
            
            if mat[mid] > tgt:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False