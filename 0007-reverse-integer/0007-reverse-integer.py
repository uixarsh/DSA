class Solution:
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1]) * (-1 if x<0 else 1)
        return temp if (temp>= (-2**(31)) and temp<=(2**(31)-1)) else 0