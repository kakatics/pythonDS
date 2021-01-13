class Stack(object):
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0
  
  def getSize(self):
    return len(self.stack)

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    if self.stack:
      return self.stack.pop()

  def peek(self):
    if self.stack:
      return self.stack[-1]

  def getStack(self):
    return self.stack

