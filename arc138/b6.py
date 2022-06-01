from collections import deque

N = int(input())
A = deque(list(map(int, input().split())))
flip_flag = 0

while len(A):
    if A[-1] == flip_flag:
        A.pop()
    elif A[0] == flip_flag:
        A.popleft()
        flip_flag = 1 - flip_flag
    else:
        print('No')
        exit()

print('Yes')

