class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def solve(arr, k, idx):
            if len(arr) == 1:
                return arr[0]
            
            idx = (idx+k-1) % len(arr)
            arr.pop(idx)
            return solve(arr, k, idx)

        arr = [i+1 for i in range(n)]
        return solve(arr, k, 0)