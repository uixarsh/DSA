class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        start_ptr = 0
        end_ptr = N-1

        while start_ptr<end_ptr:
            s[start_ptr], s[end_ptr] = s[end_ptr], s[start_ptr]
            start_ptr +=1
            end_ptr -=1