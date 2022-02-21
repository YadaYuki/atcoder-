import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
good_num_count = [A[0]-1] # A[i]以下の良い数字の数

for i in range(N-1):
    good_num_count.append(good_num_count[-1]+(A[i+1]-A[i]-1))


ans = []
for _ in range(Q):
    k = int(input())
    if k > good_num_count[-1]:
        ans.append(A[-1] + k - good_num_count[-1])
    else:
        i = bisect.bisect_left(good_num_count,k)
        ans.append(A[i] - (good_num_count[i] - k+1))

for _ in range(Q):
    print(ans[_])