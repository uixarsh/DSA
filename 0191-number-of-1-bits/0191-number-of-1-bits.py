class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            bit = n % 2
            if bit:
                cnt+=1
            n //= 2

        return cnt

        