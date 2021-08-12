from collections import deque
S = input()
queue = deque()
flag = 0
for c in S:
  if c == "R":
    flag = 1-flag
  else :
    if flag == 0:
      queue.append(c)
    elif flag == 1:
      queue.appendleft(c)

if flag == 1:
  queue.reverse()

print(queue)

