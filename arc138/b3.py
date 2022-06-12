from collections import deque
N = int(input())
A = deque(list(map(int,input().split())))
flip_flag = False
while len(A) != 0:
    if A[-1] == flip_flag:
        A.pop()
    elif A[0] == flip_flag:
        A.popleft()
        flip_flag = not flip_flag
    else:
        print("No")
        exit()

print("Yes")