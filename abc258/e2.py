N,Q,X = map(int,input().split())
W = list(map(int,input().split()))
query = [int(input()) for i in range(Q)]
potate_cnt_from_i = [-1 for i in range(N)] # i番目の箱
cyclic_graph = [-1 for i in range(N)]  # next vertex
N_base = N * (X//sum(W))
X %= sum(W)

cur_weight = 0
r = 0
for l in range(N):
    if l == 0:
        cnt = 0
        while cur_weight < X:
            cur_weight += W[r]
            cnt += 1
            r = (r+1) % N
        potate_cnt_from_i[l] = cnt
        cyclic_graph[l] = r
    else:
        cur_weight -= W[l-1]
        cnt = potate_cnt_from_i[l-1] - 1
        while cur_weight < X:
            cur_weight += W[r]
            cnt += 1
            r = (r+1) % N
        potate_cnt_from_i[l] = cnt
        cyclic_graph[l] = r


visited = [False] * N
v = 0
while not visited[v]:
    visited[v] = True
    v = cyclic_graph[v]

cyclic_start = v
v = 0
non_cyclics = []
while v != cyclic_start:
    non_cyclics.append(v)
    v = cyclic_graph[v]

cyclics = [cyclic_start]
v = cyclic_graph[cyclic_start]
while v != cyclic_start:
    cyclics.append(v)
    v = cyclic_graph[v]
ans = []

for i in range(Q):
    k = query[i]
    if k <= len(non_cyclics):
        potate = non_cyclics[k-1]
        ans.append(potate_cnt_from_i[potate])
    else:
        k -= len(non_cyclics)
        poptate_idx = (k-1) % len(cyclics)
        potate = cyclics[poptate_idx]
        ans.append(potate_cnt_from_i[potate])


for a in ans:
    print(a + N_base)