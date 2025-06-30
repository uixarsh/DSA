class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for ele in nums:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele]+=1
        
        found = []
        for key, value in d.items():
            if value > len(nums)//3:
                found.append(key)

        return found
