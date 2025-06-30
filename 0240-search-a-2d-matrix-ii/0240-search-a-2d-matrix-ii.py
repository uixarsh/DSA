class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for row_idx in range(m):
            col_idx = self.BS(matrix[row_idx], target)
            if col_idx != -1:
                return True
        
        return False

    def BS(self, arr, tgt):
        start = 0
        end = len(arr) - 1
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid] == tgt:
                return mid
            
            if arr[mid] > tgt:
                end = mid-1
            
            else:
                start = mid+1

        return -1