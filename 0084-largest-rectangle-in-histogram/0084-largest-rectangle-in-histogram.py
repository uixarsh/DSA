class Solution:
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