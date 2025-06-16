class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        L = [[0] *(n+1) for i in range(m+1)]
        
        # for i in range(m+1):
        #     L[i][0] = 0
        
        # for j in range(n+1):
        #     L[0][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        
        return L[m][n]