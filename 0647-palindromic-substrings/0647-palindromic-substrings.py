class Solution:
    def countSubstrings(self, s: str) -> int:
        ptr = 0
        d = []
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                d.append(s[i:j])
        
        pal_d = []
        for ele in d:
            if ele == ele[::-1]:
                pal_d.append(ele)

        return len(pal_d)