class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        palindromes = set()
        
        def expand_around_center(left: int, right: int):
            while left >= 0 and right < N and s[left] == s[right]:
                palindromes.add(s[left:right+1])
                left -= 1
                right += 1
        
        for i in range(N):
            expand_around_center(i, i)     # Odd length
            expand_around_center(i, i + 1) # Even length
        
        return max(palindromes, key=len)