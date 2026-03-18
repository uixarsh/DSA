class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        mpp = {}

        for ele in p:
            if ele not in mpp:
                mpp[ele] = 1
            else:
                mpp[ele] += 1
        
        cnt = len(mpp)
        ans = []
        i = 0
        j = 0

        while j<n:
            curr_ele = s[j]
            if curr_ele in mpp:
                mpp[curr_ele] -= 1
                if mpp[curr_ele] == 0:
                    cnt -= 1

            if (j-i+1) == m:
                if cnt == 0:
                    ans.append(i)
                if s[i] in mpp:
                    mpp[s[i]] += 1
                    if mpp[s[i]] == 1:
                        cnt+=1
                i+=1
            j+=1

        return ans