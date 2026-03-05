class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0

        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    start0 += 1
                if ch != '1':
                    start1 += 1
            else:
                if ch != '1':
                    start0 += 1
                if ch != '0':
                    start1 += 1

        return min(start0, start1)