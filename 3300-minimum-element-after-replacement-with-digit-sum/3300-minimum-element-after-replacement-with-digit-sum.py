class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_ele = float("inf")
        for i in range(len(nums)):
            min_ele = min(min_ele, nums[i])
            if nums[i] > 9:
                temp = 0
                for ele in str(nums[i]):
                    temp+=int(ele)
                nums[i] = temp
                min_ele = min(min_ele, temp)

        return min_ele if min_ele != float("inf") else -1