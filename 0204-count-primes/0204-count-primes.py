class Solution:
    def countPrimes(self, limit: int) -> int:
        if limit < 3:
            return 0
        if limit == 3:
            return 1

        notPrime = [0 for _ in range(((limit >> 1) + 7) >> 3)]
        count = 2
        for n in range(5, limit, 6):
            if not (notPrime[n >> 4] & (1 << ((n >> 1) & 7))):
                count += 1
                for x in range(n * n, limit, n + n):
                    notPrime[x >> 4] |= 1 << ((x >> 1) & 7)

            nPlus2 = n + 2
            if nPlus2 >= limit:
                break

            if not (notPrime[nPlus2 >> 4] & (1 << ((nPlus2 >> 1) & 7))):
                count += 1
                for x in range(nPlus2 * nPlus2, limit, nPlus2 + nPlus2):
                    notPrime[x >> 4] |= 1 << ((x >> 1) & 7)

        return count