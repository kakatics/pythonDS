class IsEmptyError(Exception):
  pass

class Node(object):
  def __init__(self, data, _next):
    self.data = data
    self._next = _next

class SLLStack(object):
  def __init__(self):
    self.head = None
    self.size = 0

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def push(self, data):
    self.head = Node(data, self.head)
    self.size += 1

  def pop(self):
    if self.isEmpty() == True:
      raise IsEmptyError("Queue is empty!")

    result = self.head.data
    self.head = self.head._next
    self.size -= 1
    return result

  def top(self):
    if self.size == True:
      return

    return self.head.data

s = SLLStack()
s.pop()
