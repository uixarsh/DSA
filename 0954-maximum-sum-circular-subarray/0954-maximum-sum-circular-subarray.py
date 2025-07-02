class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)
        max_sum = float('-inf')
        total_sum = 0
        curr_sum = 0
        min_sum = float('inf')
        
        # 1. Find maxSum in Non-circular way (Kadane's algorithm)
        for i in range(n):
            curr_sum += arr[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        # 2. Total sum of array
        total_sum = sum(arr)
        
        # 3. Find minSum in Non-circular way
        curr_min = arr[0]
        min_sum = arr[0]
        for i in range(1, n):
            curr_min = min(curr_min + arr[i], arr[i])
            min_sum = min(min_sum, curr_min)
        
        # 4. Calculate maxSum in Circular array
        max_sum_circular = total_sum - min_sum
        
        # 5. If all elements are negative, max_sum_circular can become 0
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, max_sum_circular)