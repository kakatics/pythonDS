class Queue(object):
  def __init__(self):
    self.queue = []

  def enqueue(self, data):
    self.queue.append(data)

  def dequeue(self):
    data = self.queue[0]
    del self.queue[0]
    return data

  def peek(self):
    return self.queue[0]

  def getSize(self):
    return len(self.queue)

  def printQueue(self):
    for i in self.queue:
      print(i)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print("Size of the queue:", queue.getSize())
queue.printQueue()
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Size of the queue:", queue.getSize())
queue.printQueue()
