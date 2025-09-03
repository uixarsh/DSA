class MyQueue:

    def __init__(self):
        self.__arr = []

    def push(self, x: int) -> None:
        self.__arr.append(x)

    def pop(self) -> int:
        return self.__arr.pop(0)

    def peek(self) -> int:
        return self.__arr[0]

    def empty(self) -> bool:
        return len(self.__arr) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()