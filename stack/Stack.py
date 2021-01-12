class Stack(object):
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    elem = self.stack[-1]
    del self.stack[-1]
    return elem

  def peek(self):
    return self.stack[-1]

  def getSize(self):
    return len(self.stack)

  def printStack(self):
    for i in range(len(self.stack)-1, -1, -1):
      print(self.stack[i])


stack = Stack()

print("Size of the Stack:", stack.getSize())
stack.push(1)
stack.push(3)
stack.push(5)
stack.printStack()
print("Size of the Stack:", stack.getSize())
stack.push(7)
stack.push(9)
stack.printStack()
print("Size of the Stack:", stack.getSize())
print("Pop:", stack.pop())
print("Size of the Stack:", stack.getSize())
print("Peek:", stack.peek())
print("Size of the Stack:", stack.getSize())
