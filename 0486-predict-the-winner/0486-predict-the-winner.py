class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(l, r):
            if l == r:
                return nums[l]

            take_left = nums[l] - solve(l + 1, r)
            take_right = nums[r] - solve(l, r - 1)

            return max(take_left, take_right)

        return solve(0, len(nums) - 1) >= 0