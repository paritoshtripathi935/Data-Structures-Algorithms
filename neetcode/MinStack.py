class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimum_stack or val <= self.minimum_stack[-1]:
            self.minimum_stack.append(val)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self) -> None:
        if self.isEmpty():
            return

        if self.stack[-1] == self.minimum_stack[-1]:
            self.minimum_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return -1 

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minimum_stack:
            return -1 

        return self.minimum_stack[-1]

leetcode_link = 'https://leetcode.com/problems/min-stack/submissions/1171591469'

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
