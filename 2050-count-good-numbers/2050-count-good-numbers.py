class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        o = n//2    # Total Odd Places
        e = n//2 + n%2  # Total Even Places
        # return (self.power(5,e) * self.power(5,o)) % self.mod
        total = (pow(5,e,mod) * pow(4,o,mod)) % mod
        return total

    # def power(self, x, y):
    #     if y == 1:
    #         return x
    #     ans = self.power(x, y//2)
    #     ans*=ans
    #     ans = ans%self.mod
    #     if y % 2 != 0:
    #         ans = ans * x
    #         ans = ans%self.mod
    #     return ans
