from collections import deque

# Queues are FIFO (First In First Out) data structures
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Removing elemnts from the list in order of their entrance FIFO

queue.popleft() #removes 1 - the element that was enetered first
print(queue)