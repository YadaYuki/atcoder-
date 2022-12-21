N = int(input())
a = list(map(int,input().split()))

a_w_idx = [[a[i-1],i] for i in range(1,N+1)]

N_eq = 0
for i in range(N):
    ai,idx = a_w_idx[i]
    if ai == idx:
        N_eq += 1
# print(N_eq)
ans = 0
for i in range(N):
    ai,idx = a_w_idx[i]
    # print(ai,idx)
    if ai != idx:
        if ai <= N:
            if idx == a[ai-1]:
                ans += 1
                # print(idx,ai)

ans //= 2
ans += N_eq * (N_eq-1) // 2

print(ans)