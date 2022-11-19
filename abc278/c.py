from collections import defaultdict

N,Q = map(int,input().split())

followers = defaultdict(set)

for i in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        followers[b].add(a)
    elif t == 2:
        if a in followers[b]:
            followers[b].remove(a)
    elif t == 3:
        if a in followers[b] and b in followers[a]:
            print("Yes")
        else:
            print("No")


