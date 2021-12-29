class MinStack:

    def __init__(self):
        # 列表的尾部相当于栈顶
        self.stack = []
        self.min_stack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))  # 保证最后一个是最小的

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if 0 == len(self.stack):
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    print(obj.stack, obj.min_stack)
    obj.pop()
    print(obj.stack, obj.min_stack)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3, param_4)
