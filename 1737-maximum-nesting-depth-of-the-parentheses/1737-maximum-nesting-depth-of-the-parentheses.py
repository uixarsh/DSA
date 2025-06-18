class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        actual_count = 0
        for chr in s:
            if chr == '(':
                actual_count+=1
            
            if chr == ')':
                if actual_count > max_count:
                    max_count = actual_count
                actual_count -=1

        return max_count
            