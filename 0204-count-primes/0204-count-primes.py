max_n = int(5 * 1e6)

primes = [True for _ in range(max_n + 1)]
primes[0], primes[1] = False, False
count_primes = [0 for _ in range(max_n + 1)]

count = 0
for i in range(2, max_n + 1):
    if primes[i]:
        count += 1
        
        for j in range(i * i, max_n + 1, i):
            primes[j] = False

    count_primes[i] = count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        return count_primes[n-1]