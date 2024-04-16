from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.freq_map = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq_map[val] += 1

    def pop(self) -> int:
        max_freq = max(self.freq_map.values())
        max_freq_elements = [key for key, value in self.freq_map.items() if value == max_freq]
        # Find the most recently added element among those with max frequency
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freq_elements:
                el = self.stack[i]
                del self.stack[i]
                self.freq_map[el] -= 1
                if self.freq_map[el] == 0:
                    del self.freq_map[el]
                return el