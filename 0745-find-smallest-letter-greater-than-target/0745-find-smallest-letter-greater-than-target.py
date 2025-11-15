class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        res = letters[0]
        n = len(letters)
        start = 0
        end = (n-1)
        
        while start <= end:
            mid = start + (end-start)//2
                
            if ord(letters[mid]) > ord(target):
                res = letters[mid]
                end = mid-1
            
            else:
                start = mid+1

        return res