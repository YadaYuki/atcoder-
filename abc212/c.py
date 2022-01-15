N,M = map(int,input().split())
A = list( map(int,input().split()))
B = list( map(int,input().split()))

BIG = 10 ** 10
j = 0
ans = BIG

A.sort()
B.sort()


for i in range(N):
    # Fix A[i]
    while True:
        if j == M-1:
            ans = min(ans,abs(A[i] - B[j]))
            break
        if abs(A[i] - B[j]) < abs(A[i] - B[j+1]):
            ans = min(ans,abs(A[i] - B[j]))
            break
        else:
            j += 1

print(ans)