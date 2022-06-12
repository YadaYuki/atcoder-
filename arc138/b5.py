N = int(input())
A = list(map(int, input().split()))
flip_flag = 0

while len(A):
    if A[-1] == flip_flag:
        A.pop()
    elif A[0] == flip_flag:
        A.pop(0)
        flip_flag = 1 - flip_flag
    else:
        print('No')
        exit()

print('Yes')

