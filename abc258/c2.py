N,Q = map(int,input().split())
S = list(input())

head_idx = 0
tail_idx = N - 1
for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        tail_idx -= x
        if tail_idx < 0:
            tail_idx += N
        head_idx = tail_idx + 1
        if head_idx == N:
            head_idx = 0
    else:
        idx = head_idx + x - 1
        if idx >= N:
            idx -= N
        print(S[idx])

