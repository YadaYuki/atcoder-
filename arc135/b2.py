



N = int(input())
S = list(map(int, input().split()))
A = [0] * (N + 2)
for s in [1, 2, 3]:
    cur = 0
    low = 0
    for i in range(s,N,3):
        cur += S[i] - S[i-1]
        A[i+2] = cur
        low = min(low, cur)
    
    for i in range(s-3,N,3):
        A[i+2] += abs(low)
add = S[0] - sum(A[0:3])
if add < 0:
    print("No")
    exit()

print("Yes")

for i in range(N+2):
    if i % 3 == 0:
        A[i] += add
    
print(*A)

