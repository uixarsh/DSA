class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.get_combinations(0, path, res, n, k)
        return res

    def get_combinations(self, start : int, path : List[int], res : List[List[int]], n : int, k : int):
        
        # Base Condition
        if k==0:
            if sum(path) == n:
                res.append(path[:])
            return
        
        # Control Statement
        for i in range(start+1, 10):
            path.append(i)
            self.get_combinations(i, path, res, n, k-1)
            path.pop()