N = int(input())
BIG = 10**9 + 7
max_L, min_R =  0,BIG
for _ in range(N):
    L, R = map(int, input().split())
    max_L = max(max_L, L)
    min_R = min(min_R, R)
    if max_L <= min_R:
        print(0)
    else:
        print(-(-(max_L - min_R) // 2))
    

