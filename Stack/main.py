class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()  # [1,2,3,4,5]
        return "stack is empty"

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


def reverseString(str):
    s = Stack()
    revStr = ""
    for char in str:
        s.push(char)
    while not s.is_empty():
        revStr += s.top()
        s.pop()
    return revStr


def decToBinary(n):
    s = Stack()
    while n > 0:
        remainder = n % 2
        s.push(remainder)
        n //= 2
    binaryStr = ""
    while not s.is_empty():
        binaryStr += str(s.top())
        s.pop()
    return binaryStr


s = Stack()
s.push(30)
s.push(20)
s.push(10)
s.pop()
print(s.size(), s.top())
while not s.is_empty():
    print(s.top())
    s.pop()
