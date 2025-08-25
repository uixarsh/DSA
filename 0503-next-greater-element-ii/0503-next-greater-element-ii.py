class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        n = len(nums)
        nge = [-1]*n

        for i in range(2*n-1, -1, -1):
            while len(st) != 0 and st[-1] <= nums[i%n]:
                st.pop()
            
            if i<n:
                nge[i] = -1 if len(st) == 0 else st[-1]

            st.append(nums[i%n])

        return nge