class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Cretae LCA function
def lca(root, n1, n2):
  # Base Case
  if root is None:
    return None

  if root.data == n1 or root.data == n2:
    return root

  # Recursive Case
  left = lca(root.left, n1, n2)
  right = lca(root.right, n1, n2)

  if left and right:
    return root
  if left:
    return left
  else:
    return right

# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print(lca(root, 8,15).data)
