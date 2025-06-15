class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(s, 0, len(s)-1)
    
    def rev(self, s: List[str], start_ptr: int, end_ptr: int):
        if end_ptr < start_ptr:
            return
        s[start_ptr], s[end_ptr] = s[end_ptr], s[start_ptr]
        self.rev(s, start_ptr+1, end_ptr-1)