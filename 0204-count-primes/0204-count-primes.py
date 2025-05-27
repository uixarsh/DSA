class Solution:
    def countPrimes(self, n: int) -> int:
        def sieveOfEratosthenes(N):
            if N>2:
                sieve = [True]*(N)
                sieve[0] = False
                sieve[1] = False
                for i in range(2, int(N**0.5) + 1):
                    if sieve[i]:
                        for m in range(i*i, N, i):
                            sieve[m] = False
                res = []
                for idx, number in enumerate(sieve):
                    if number: 
                        res.append(idx)
                return len(res)
            return 0
        
        return (sieveOfEratosthenes(n))