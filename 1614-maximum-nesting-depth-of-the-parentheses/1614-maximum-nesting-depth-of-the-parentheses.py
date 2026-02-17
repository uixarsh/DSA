class Solution:
    def maxDepth(self, s: str) -> int:
        max_len = 0
        st = []
        for ele in s:
            if ele == '(':
                st.append(ele)
                max_len = max(max_len, len(st))
            elif ele == ')':
                st.pop()

        return max_len