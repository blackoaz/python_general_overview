from collections import deque
history = deque()

# adding values to the stack - LIFO
history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(history)

# removing the last entered value in the stack - LIFO
history.popleft() 
history.popleft()
print(history) 