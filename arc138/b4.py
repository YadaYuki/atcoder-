from  collections import deque
N = int(input())
A = deque(list(map(int,input().split())))
flip = 0

while len(A):
    if A[-1] == flip:
        A.pop()
    elif A[0] == flip:
        A.popleft()
        flip = 1-flip
    else:
        print("No")
        exit()

print("Yes")
