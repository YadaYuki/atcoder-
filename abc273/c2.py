from bisect import bisect_right
N = int(input())
A = list(map(int,input().split()))
A_sorted = sorted(list(set(A)))
k_to_ans = [0 for i in range(N)]
for a in A:
    k = bisect_right(A_sorted,a)
    k_to_ans[len(A_sorted)-k] += 1
for k in k_to_ans:
    print(k)


