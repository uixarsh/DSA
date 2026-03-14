class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        count = 0
        ans = ""

        def backtrack(curr):
            nonlocal count, ans
            
            if len(curr) == n:
                count += 1
                if count == k:
                    ans = curr
                return
            
            for ch in chars:
                if curr and curr[-1] == ch:
                    continue
                
                backtrack(curr + ch)
                
                if ans:
                    return
        
        backtrack("")
        return ans