from collections import defaultdict
N,Q = map(int,input().split())

a = list(map(int,input().split()))

a_map = defaultdict(list) # {i:[iが登場する位置]}

for i in range(N):
    a_map[a[i]].append(i)

query = [list(map(int,input().split())) for _ in range(Q)]

for i in range(Q):
    x,k = query[i]
    if len(a_map[x]) < k:
        print(-1)
    else:
        print(a_map[x][k-1]+1)
    