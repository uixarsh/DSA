class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        x = [[0]*n for i in range(m)]
        
        for col in range(n):
            for row in range(m):
                if matrix[row][col] == "1":
                    x[row][col] = int(matrix[row][col]) + x[row-1][col]
        
        larg = 0
        for i in range(len(x)):
            larg = max(larg, self.largestRectangleArea(x[i]))
        
        return larg

    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        maxArea = 0
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                ele = st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxArea = max(maxArea, (heights[ele]* (nse-pse-1)))
            st.append(i)

        # If elements got left over
        while st:
            ele = st.pop()
            nse = n
            pse = st[-1] if st else -1
            maxArea = max(maxArea, (heights[ele]* (nse-pse-1)))

        return maxArea