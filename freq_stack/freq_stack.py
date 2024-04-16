from collections import deque
class FreqStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        max_occ = max([self.stack.count(i) for i in self.stack])
        elements = [i for i in self.stack if self.stack.count(i) == max_occ]
        index = max([i for i, value in enumerate(self.stack) if value in elements])
        el = self.stack[index]
        del self.stack[index]
        return el


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()