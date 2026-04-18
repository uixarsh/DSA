class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = reversed(str(n))
        y = ""
        for ele in x:
            y+=ele

        return abs(int(y) - n)
        