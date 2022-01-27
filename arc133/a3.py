# A[i] > A[i+1]を初めてみたすようなA[i]がx
# 単調増加列の場合は、最も後ろの値がx

x = -1

N = int(input())
A = list(map(int,input().split()))


for i in range(N-1):
    if A[i] > A[i+1]:
        x = A[i]
        break

if x == -1:
    x = A[-1]


ans = [A[i] for i in range(N) if A[i] != x]
print(*ans)