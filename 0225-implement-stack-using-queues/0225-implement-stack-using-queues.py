class MyStack:

    def __init__(self):
        self.__arr = []

    def push(self, x: int) -> None:
        self.__arr.append(x)

    def pop(self) -> int:
        return self.__arr.pop()

    def top(self) -> int:
        return self.__arr[-1]

    def empty(self) -> bool:
        return len(self.__arr) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()