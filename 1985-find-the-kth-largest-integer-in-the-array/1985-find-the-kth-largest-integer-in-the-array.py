class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        x = [int(i) for i in nums]
        x = sorted(x, reverse=True)
        return str(x[k-1])