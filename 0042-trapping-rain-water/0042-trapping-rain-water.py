class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        def prefixMax() -> list:
            prefix_max = [-1]*n
            prefix_max[0] = height[0]
            for i in range(1,n):
                prefix_max[i] = max(prefix_max[i-1], height[i])
            return prefix_max

        def suffixMax() -> list:
            suffix_max = [-1]*n
            suffix_max[n-1] = height[n-1]
            for i in range(n-2, -1, -1):
                suffix_max[i] = max(suffix_max[i+1], height[i])
            return suffix_max

        left_max = prefixMax()
        rgt_max = suffixMax()

        for i in range(n):
            l_max = left_max[i]
            r_max = rgt_max[i]

            if height[i] < r_max and height[i] < l_max:
                total+= min(l_max, r_max) - height[i]

        return total