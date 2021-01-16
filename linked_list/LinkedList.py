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
      while currentNode.nextNode:
        currentNode = currentNode.nextNode
      currentNode.nextNode = newNode

  def insertAfterNode(self, prevNode, data):
    newNode = Node(data)
    currentNode = self.head

    while currentNode.data != prevNode and currentNode:
      currentNode = currentNode.nextNode
    
    if currentNode is None:
      return

    newNode.nextNode = currentNode.nextNode
    currentNode.nextNode = newNode
    self.size += 1


  def getSize(self):
    return self.size

  def remove(self, data):
    if self.size <= 0:
      return

    currentNode = self.head
    previousNode = None

    if currentNode.data == data:
      self.head = currentNode.nextNode
      self.size -= 1
      return

    while currentNode:
      if currentNode.data != data:
        previousNode = currentNode
        currentNode = currentNode.nextNode
      else:
        previousNode.nextNode = currentNode.nextNode
        self.size -= 1
        break

  def removeAtPosition(self, pos):
    if self.size <= 0 or self.size <= pos:
      return

    currentNode = self.head
    previousNode = None

    if pos == 0:
      self.head = currentNode.nextNode
      self.size -= 1
      return

    for i in range(pos):
      previousNode = currentNode
      currentNode = currentNode.nextNode

    previousNode.nextNode = currentNode.nextNode
    self.size -= 1

  def traverseList(self):
    if self.size <= 0:
      return

    currentNode = self.head

    while currentNode.nextNode is not None:
      print("%d -> " % currentNode.data, end="")
      currentNode = currentNode.nextNode
    print(currentNode.data)

