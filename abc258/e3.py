


N,Q,X = map(int,input().split())
W = list(map(int,input().split()))
Ks = [int(input()) for i in range(Q)]
arrows = [-1 for i in range(N)]
potate_cnts = [-1 for i in range(N)]
K_base = (X // sum(W)) * N
X %= sum(W)
r = 0
cur_weight = 0
cnt = 0
for l in range(N):
    while cur_weight < X:
        cur_weight += W[r]
        r = (r+1)%N
        cnt += 1
    
    arrows[l] = r
    potate_cnts[l] = cnt + K_base
    cnt -= 1
    cur_weight -= W[l]

# cyclic check
visited = [False] * N
c = 0
while not visited[c]:
    visited[c] = True
    c = arrows[c]

cyclic_start = c
cyclics = []
while True:
    cyclics.append(c)
    c = arrows[c]
    if c == cyclic_start:
        break

non_cyclics = []
c = 0
while c != cyclic_start:
    non_cyclics.append(c)
    c = arrows[c]
ans = list()
for k in Ks:
    if k <= len(non_cyclics):
        ans.append(potate_cnts[non_cyclics[k-1]])
    else:
        k -= len(non_cyclics)
        potate_idx_in_cyclics = (k-1)%len(cyclics)
        ans.append(potate_cnts[cyclics[potate_idx_in_cyclics]])

for a in ans:
    print(a)