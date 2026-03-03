class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(cleaned)

        def driver(i):
            nonlocal cleaned, n

            if i >= n // 2:
                return True
            
            if cleaned[i] != cleaned[n-i-1]:
                return False
            
            return driver(i+1)

        return driver(0)