class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0

        mpp = {}

        if n == 0:
            return 0
            
        ans = 1

        while j<n:
            if s[j] not in mpp:
                mpp[s[j]] = 1
            else:
                mpp[s[j]] += 1

            while len(mpp) != (j-i+1) and i<=j:
                mpp[s[i]] -= 1
                if not mpp[s[i]]:
                    mpp.pop(s[i])
                i+=1

            if len(mpp) == (j-i+1):
                ans = max(ans, (j-i+1))

            j+=1

        return ans