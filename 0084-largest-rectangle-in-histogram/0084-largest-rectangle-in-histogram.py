class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        def next_smaller_ele() -> list:
            st = []
            d = [n] * n
            for i in range(n - 1, -1, -1):
                while st and heights[i] <= heights[st[-1]]:
                    st.pop()
                if st:
                    d[i] = st[-1]
                st.append(i)
            return d

        def prev_smaller_ele() -> list:
            st = []
            d = [-1] * n
            for i in range(n):
                while st and heights[i] <= heights[st[-1]]:
                    st.pop()
                if st:
                    d[i] = st[-1]
                st.append(i)
            return d

        nse = next_smaller_ele()
        pse = prev_smaller_ele()

        area = 0
        for i in range(n):
            area = max(area, heights[i] * (nse[i] - pse[i] - 1))
        
        return area
