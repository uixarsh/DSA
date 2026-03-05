class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def nCr(n, r):
            if r > n:
                return 0
            
            r = min(r, n-r)   # symmetry optimization nCr = nCn-r
            res = 1

            for i in range(r):
                res = res * (n-i)
                res = res // (i+1)
            
            return res

        ans = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(nCr(i, j))
            ans.append(temp)

        return ans