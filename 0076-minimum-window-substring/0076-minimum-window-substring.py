class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n:
            return ""

        mpp = {}

        for ele in t:
            if ele not in mpp:
                mpp[ele] = 1
            else:
                mpp[ele] += 1
        
        cnt = len(mpp)
        min_lent = float("inf")
        start = 0

        i = 0
        j = 0

        while j<n:
            if s[j] in mpp:
                mpp[s[j]] -= 1

                if mpp[s[j]] == 0:
                    cnt-=1
            
            while not cnt:
                if (j-i+1) < min_lent:
                    min_lent = (j-i+1)
                    start = i
                if s[i] in mpp:
                    mpp[s[i]] += 1
                    if mpp[s[i]] > 0:
                        cnt+=1
                i+=1
            j+=1
        
        return "" if min_lent == float('inf') else s[start: start + min_lent]
                