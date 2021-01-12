class Node(object):
  def __init__(self, data):
    self.data = data
    self.nextNode = None
    self.prevNode = None

class DoublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, data):
    newNode = Node(data)
    self.size += 1

    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      currentNode = self.tail
      self.tail = newNode
      self.tail.prevNode = currentNode
      self.tail.prevNode.nextNode = self.tail

  def prepend(self, data):
    newNode = Node(data)
    self.size += 1
    
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      currentNode = self.head
      self.head = newNode
      self.head.nextNode = currentNode
      self.head.nextNode.prevNode = self.head

  def print_list(self):
    print("---List---")
    currentNode = self.head
    while currentNode.nextNode is not None:
      print("%d -> " % currentNode.data, end="")
      currentNode = currentNode.nextNode
    print("%d" % currentNode.data)
  
  def print_list_reverse(self):
    print("---Reverse List---")
    currentNode = self.tail
    while currentNode.prevNode is not None:
      print("%d -> " % currentNode.data, end="")
      currentNode = currentNode.prevNode
    print("%d" % currentNode.data)

  def getSize(self):
    return self.size


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(3)
dllist.append(-23)
dllist.append(56)
dllist.append(354)
dllist.append(0)
dllist.prepend(999)

dllist.print_list()
dllist.print_list_reverse()
print("Size of the list:",dllist.getSize())

