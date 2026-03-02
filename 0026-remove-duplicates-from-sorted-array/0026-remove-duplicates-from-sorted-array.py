class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = set(nums)
        arr = []
        for i in st:
            arr.append(i)
        arr.sort()
        nums[:] = arr