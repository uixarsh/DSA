from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Stores indices
        ans = []
        n = len(nums)
        i, j = 0, 0

        while j < n:
            # 1. Calculation: Maintain Monotonic Deque (remove smaller elements from back)
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            # 2. Window Size: Check if we have hit size K
            if (j - i + 1) == k:
                # 3. Answer: Maximum is at the front
                ans.append(nums[q[0]])
                # 4. Slide Window: Remove index if it's sliding out
                if q[0] == i:
                    q.popleft()
                i += 1
            j += 1

        return ans
