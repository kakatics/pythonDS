class Node(object):
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.size = 0

  def insertAtStart(self, data):
    newNode = Node(data)
    self.size += 1

    if self.head is None:
      self.head = newNode
    else:
      newNode.nextNode = self.head
      self.head = newNode

  def insertAtEnd(self, data):
    newNode = Node(data)
    currentNode = self.head
    self.size += 1

    if self.head is None:
      self.head = newNode
    else:
      while currentNode.nextNode is not None:
        currentNode = currentNode.nextNode
      currentNode.nextNode = newNode

  def getSize(self):
    return self.size

  def remove(self, data):
    if self.size <= 0:
      return

    currentNode = self.head
    previousNode = None

    while currentNode is not None:
      if currentNode.data != data:
        previousNode = currentNode
        currentNode = currentNode.nextNode
      else:
        previousNode.nextNode = currentNode.nextNode
        self.size -= 1
        break

  def traverseList(self):
    if self.size <= 0:
      return

    currentNode = self.head

    while currentNode.nextNode is not None:
      print("%d -> " % currentNode.data, end="")
      currentNode = currentNode.nextNode
    print(currentNode.data)


ll = LinkedList()
ll.traverseList()
ll.insertAtEnd(1)
ll.insertAtStart(3)
ll.insertAtStart(5)
ll.insertAtStart(7)
ll.insertAtStart(9)
ll.traverseList()
print(ll.getSize())
ll.remove(5)
ll.traverseList()
print(ll.getSize())
ll.insertAtEnd(99)
ll.traverseList()
print(ll.getSize())
ll.insertAtEnd(999)
ll.traverseList()
print(ll.getSize())
ll.remove(78)
ll.remove(999)
ll.traverseList()
print(ll.getSize())
