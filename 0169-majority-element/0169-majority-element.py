class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = dict()

        for i in range(n):
            if nums[i] not in mpp:
                mpp[nums[i]] = 1
            else:
                mpp[nums[i]] +=1

        for key, val in mpp.items():
            if val > n//2:
                return key
        
        return -1