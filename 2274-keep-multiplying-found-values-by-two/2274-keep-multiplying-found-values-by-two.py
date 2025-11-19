class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Brute Force
        ele = original
        n = len(nums)
        x = sorted(nums)
        
        for i in range(n):
            if x[i] == ele:
                ele *= 2

        return ele