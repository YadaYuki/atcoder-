N = int(input())
A = list(map(int,input().split()))
ans = [0 for _ in range(2*N+1)]

for k in range(1,2*N+1):
    ans[k] = ans[A[int((k+1)/2)-1]-1] + 1

for a in ans:
    print(a)