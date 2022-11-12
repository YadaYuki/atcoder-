N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
remove_max = -1
cur = A[0]
for i in range(N-1):
    if (A[i] == A[i+1]) or (A[i] + 1 == A[i+1]):
        cur += A[i+1]
    else:
        remove_max = max(remove_max,cur)
        cur = A[i + 1]

remove_max = max(remove_max,cur)
if remove_max == sum(A): # 単調増加をここで
    print(0)
    exit()

if A[0] == 0 and A[-1] == M-1:
    for i in range(N-1):
        if not ((A[i] == A[i+1]) or (A[i] + 1 == A[i+1])):
            break
        cur += A[i+1]
remove_max = max(remove_max,cur)
print(sum(A) - remove_max)

