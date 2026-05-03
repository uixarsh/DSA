class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        new_s = s[:]

        while n:
            new_s = new_s[1:] + new_s[0]
            if new_s == goal:
                return True            
            n-=1

        return False