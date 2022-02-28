from collections import deque
from itertools import permutations
import math

# xyzをzxyに並び変える操作で,どんな並び替えも作れるという仮説を検証する
N = 4
A = [i+1 for i in range(N)]
# B = [N-i for i in range(N)]
visited = {}


def list_to_s(l):
    return ','.join(map(str, l))


queue = deque([list_to_s(A)])
while len(queue) > 0:
    s = queue.popleft()
    if s in visited:
        continue
    visited[s] = True
    a = list(map(int, s.split(',')))
    for i in range(N-2):
        a_copy = a[:]
        a_copy[i], a_copy[i+1], a_copy[i+2] = a_copy[i+2], a_copy[i], a_copy[i+1]
        queue.append(list_to_s(a_copy))

for p in permutations(A):
    if list_to_s(list(p)) not in visited:
        print(p)
        # exit()
print(visited, len(visited))
print('4,3,2,1' in visited)
