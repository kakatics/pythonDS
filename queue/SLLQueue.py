class SLLQueue(object):
  class Node(object):
    def __init__(self, data, _next):
      self.data = data
      self._next = _next

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def enqueue(self, data):
    newNode = self.Node(data, None)

    if self.isEmpty():
      self.head = newNode
    else:
      self.tail._next = newNode
    self.tail = newNode
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      return
    data = self.head.data
    self.head = self.head._next
    self.size -= 1

    if self.isEmpty():
      self.tail = None

    return data

  def first(self):
    if self.isEmpty():
      return
    return self.head.data
