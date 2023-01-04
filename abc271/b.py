N,Q = map(int,input().split())
a = list()

for i in range(N):
    La = list(map(int,input().split()))
    L = La[0]
    ai = La[1:]
    a.append(ai)
ans = list()
for i in range(Q):
    s,t = map(int,input().split())
    s-=1
    t-=1
    ans.append(a[s][t])
for a in ans:
    print(a)