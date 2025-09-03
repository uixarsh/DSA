class MyQueue:

    def __init__(self):
        self.__st1 = []
        self.__st2 = []

    def push(self, x: int) -> None:
        self.__st1.append(x)

    def pop(self) -> int:
        if not self.__st2:
            while self.__st1:
                self.__st2.append(self.__st1.pop()) 
        return self.__st2.pop()

    def peek(self) -> int:
        if not self.__st2:
            while self.__st1:
                self.__st2.append(self.__st1.pop()) 
        return self.__st2[-1]

    def empty(self) -> bool:
        return not self.__st1 and not self.__st2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()