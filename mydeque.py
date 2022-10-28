from collections import deque

fifo = deque([1, 2, 3, 4, 5])
print(fifo)

fifo.append(11)
fifo.appendleft(-11)
print(fifo)
print(fifo.pop())
print(fifo)
print(fifo.popleft())
print(fifo)
