class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.get_combinations(0, path, res, n, k)
        return res

    def get_combinations(self, start : int, path : List[int], res : List[List[int]], n : int, k : int):
        
        # Base Condition
        if k==0:
            res.append(path[:])
            return
        
        # Control Statement
        for i in range(start+1, n+1):
            path.append(i)
            self.get_combinations(i, path, res, n, k-1)
            path.pop()
