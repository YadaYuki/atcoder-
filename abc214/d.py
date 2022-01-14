N = int(input())
E = []

for _ in range(N-1):
    u,v,w = map(int,input().split())
    E.append((u-1,v-1,w))

E.sort(key = lambda x:x[2])

p = [-1 for _ in range(N)]

def find(x):
    if p[x] < 0:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        p[x] += p[y]
        p[y] = x

ans = 0

for i in range(N-1):
    u,v,w = E[i]
    ans += p[find(u)] * p[find(v)] * w
    union(u, v)

print(ans)

