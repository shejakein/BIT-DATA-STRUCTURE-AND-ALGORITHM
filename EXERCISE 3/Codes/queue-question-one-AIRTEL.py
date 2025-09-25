from collections import deque
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5"])
queue.popleft()
print("Next client:", queue[0])
