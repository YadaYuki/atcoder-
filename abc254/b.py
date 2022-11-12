N = int(input())

A = []

for i in range(N):
    A.append([None] * (i+1))
    for j in range(0,i+1):
        if j == 0 or j == i:
            A[i][j] = 1
        else:
            A[i][j] = A[i-1][j-1] + A[i-1][j]

for a in A:
    print(*a)