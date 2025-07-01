class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            # Really don't care if the num is already marked negative.
            n = abs(n)

            # If num is already marked as negative then we are certain the num repeats.
            # constraints: num repeats twice only
            # [1, n]
            if nums[n-1] < 0:
                res.append(n)

            # Track that the particular num has been checked by updating that ele against the number index.
            nums[n-1] = -nums[n-1]

        return res