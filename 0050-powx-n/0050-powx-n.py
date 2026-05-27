class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = (1/x)
            n = abs(n)

        def solve (x, n):
            if n == 0:
                return 1

            if n == 1:
                return x
            
            return solve(x*x, n//2) if n%2==0 else solve(x*x, n//2) * x

        return solve(x, n)