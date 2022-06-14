import bisect
N,Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
not_A_count = [A[0]-1]

for i in range(1,N):
    not_A_count.append(not_A_count[-1] + (A[i]-A[i-1]-1))

# print(not_A_count)
ans = []
for _ in range(Q):
    k = int(input())
    if not_A_count[-1] < k:
        ans.append(A[-1] + (k-not_A_count[-1]))
    else:
        i = bisect.bisect_left(not_A_count,k)
        ans.append(A[i] - (not_A_count[i] - k+1))


for i in ans:
    print(i)