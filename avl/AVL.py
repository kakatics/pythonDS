class Node(object):
  def __init__(self, data):
    self.data = data
    self.height = 0
    self.leftChild = None
    self.rightChild = None


class AVL(object):
  def __init__(self):
    self.root = None

  def calcHeight(self, node):
    if not node:
      return -1

    return node.height

  def calcBalance(self, node):
    if not node:
      return 0

    return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

  def rotateRight(self, node):
    print("Roatating to the right on node ", node.data)
    
    tempLeftChild = node.leftChild
    t = tempLeftChild.rightChild
    tempLeftChild.rightChild = node
    node.leftChild = t
    
    node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
    tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
    
    return tempLeftChild

  def rotateLeft(self, node):
    print("Roatating to the left on node ", node.data)
    
    tempRightChild = node.RightChild
    t = tempRightChild.leftChild
    tempRightChild.leftChild = node
    node.RightChild = t
    
    node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
    tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1

    return tempRightChild
