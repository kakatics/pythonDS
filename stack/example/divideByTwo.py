from Stack import Stack

def divideByTwo(number):
  s = Stack()

  while number > 0:
    remainder = number % 2
    s.push(remainder)
    number = number // 2

  binary = ""

  for i in range(s.getSize()):
    b = s.pop()
    binary += str(b)

  return binary
