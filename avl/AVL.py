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

