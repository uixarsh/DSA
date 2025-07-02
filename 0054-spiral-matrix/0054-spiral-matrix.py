class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, (min(m, n) + 1) // 2):
            top = i
            bottom = m - i - 1
            left = i
            right = n - i - 1

            # 1) left → right (top)
            for col in range(left, right + 1):
                d.append(matrix[top][col])

            # 2) top → bottom (right)
            for row in range(top + 1, bottom + 1):
                d.append(matrix[row][right])

            # 3) right → left (bottom)
            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    d.append(matrix[bottom][col])

            # 4) bottom → top (left)
            if left < right:
                for row in range(bottom - 1, top, -1):
                    d.append(matrix[row][left])

        return d