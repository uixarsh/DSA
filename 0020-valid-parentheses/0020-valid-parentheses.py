class Stack:
    def __init__(self):
        self.__arr = []
    
    def pushback(self, ele):
        self.__arr.append(ele)
    
    def top(self):
        if self.__arr:
            return self.__arr[-1]
        return ''
    
    def popback(self):
        if self.__arr:
            return self.__arr.pop()
        return ''
    
    def length(self):
        return len(self.__arr)

class Solution:
    def isValid(self, s: str) -> bool:
        v = Stack()
        n = len(s)

        if s[0] in ")]}" or not n:
            return False
        
        for i in range(n):
            if s[i] in '([{':
                v.pushback(s[i])
            
            elif s[i] == ')' and v.top() == '(':
                v.popback()

            elif s[i] == '}' and v.top() == '{':
                v.popback()

            elif s[i] == ']' and v.top() == '[':
                v.popback()
            
            else:
                v.pushback(s[i])

        if not v.length():
            return True
        else:
            return False
            
