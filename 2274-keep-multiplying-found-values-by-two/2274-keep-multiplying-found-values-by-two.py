class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        rslt = original
        x = sorted(set(nums))

        for i in x:
            if i == rslt:
                rslt *= 2

        return rslt