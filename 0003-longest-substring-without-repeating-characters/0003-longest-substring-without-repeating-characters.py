class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        for i in range(n):
            hsh = [0]*256
            for j in range(i,n):
                if hsh[ord(s[j])] == 1:
                    break
                lenth = j - i + 1
                max_len = max(lenth, max_len)
                hsh[ord(s[j])] = 1

        return max_len