class Solution:
    def romanToInt(self, s: str) -> int:
        mpp = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            val = mpp[s[i]]
            if i + 1 < n and val < mpp[s[i + 1]]:
                total -= val
            else:
                total += val

        return total