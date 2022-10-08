from collections import deque

N = int(input())
A = deque(list(map(int, input().split())))

flip_cnt = 0

while len(A):
    if (A[-1] == 0 and flip_cnt % 2 == 0) or (A[-1] == 1 and flip_cnt % 2 == 1):
        A.pop()
    elif (A[0] == 0 and flip_cnt % 2 == 0) or (A[0] == 1 and flip_cnt % 2 == 1):
        A.popleft()
        flip_cnt += 1
    else:
        break

if len(A):
    print("No")
else:
    print("Yes")