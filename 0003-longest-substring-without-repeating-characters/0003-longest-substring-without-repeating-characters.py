class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsh = [-1]*256
        l_ptr=0
        r_ptr=0
        max_len=0
        n=len(s)

        while r_ptr < n:
            if hsh[ord(s[r_ptr])] != -1:
                if hsh[ord(s[r_ptr])] >= l_ptr:
                    l_ptr = hsh[ord(s[r_ptr])] + 1
            lent = r_ptr - l_ptr + 1
            max_len = max(max_len, lent)
            hsh[ord(s[r_ptr])] = r_ptr
            r_ptr+=1

        return max_len