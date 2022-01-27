N = int(input())
A = list(input().split())
max_val = max(A)
min_val = min(A)

ans = []
if A[0] == min_val:
    x = max_val
else:
    x = str(0)
    for i in range(N):
        if A[i] == min_val:
            break
        else:
            x = max(x, A[i])


for i in range(N):
        if A[i] != x:
            ans.append(A[i])
print(*ans)