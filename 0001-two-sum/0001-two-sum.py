class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sum=[]
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    sum.append(j)
                    sum.append(i)
                    return sum
        