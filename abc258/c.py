N,Q = map(int,input().split())

S = list(input())

def next_char_idx(idx):
    return idx + 1 if idx != N - 1 else 0

front = 0
back = N-1

for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        back = back - x if back - x >= 0 else back - x + N
        front = next_char_idx(back)
    if t == 2:
        idx = front + (x-1) 
        if idx >= N:
            idx -= N
        print(S[idx])

# 2 12
# ku
# 1 1
# 1 1
# 1 2
# 2 1
# 2 2
# 2 2
# 2 2
# 2 2
# 1 1
# 2 2
# 1 2
# 2 1
