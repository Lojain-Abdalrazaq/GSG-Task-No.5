class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if (len(self.stack) == 0):
            print("The array is empty, can't be popped")
        else:
            self.stack.pop()

    def top(self):
        if (len(self.stack) == 0):
            print("The array is empty, there is no top")
        else:
            return self.stack[-1]

    def getMin(self):
        if (len(self.stack) == 0):
            print("The array is empty, no minimum value")
            return null
        else:
            return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()