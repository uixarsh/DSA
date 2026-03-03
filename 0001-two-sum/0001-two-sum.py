class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mpp = dict()

        for i in range(n):
            diff = target - nums[i]
            if diff in mpp:
                return [i, mpp[diff]]
            if nums[i] not in mpp:
                mpp[nums[i]] = i
            
        return []