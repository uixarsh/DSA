class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Moore's Voting Algorithm
        ( If there exists and element >N/2 times i'm certain the algo will return it)
        '''
        n = len(nums)
        ele = -1
        cnt = 0

        for i in range(n):
            if cnt == 0:
                ele = nums[i]
                cnt+=1
                continue

            if nums[i] == ele:
                cnt+=1
            else:
                cnt-=1

        return ele
