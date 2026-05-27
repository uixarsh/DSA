class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                ch = ch.lower()
                if ch not in first_upper:
                    first_upper[ch] = i

        cnt = 0

        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                cnt += 1

        return cnt
