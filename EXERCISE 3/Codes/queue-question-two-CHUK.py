from collections import deque
queue = deque(["Patient1","Patient2","Patient3","Patient4","Patient5","Patient6","Patient7","Patient8","Patient9"])
queue.popleft()
queue.popleft()
print("Third patient served:",queue[0])