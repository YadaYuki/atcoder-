from collections import deque,defaultdict


Q = int(input())

S = deque()

ans = []

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        c = query[1]
        x = int(query[2])
        S.append([c,x])
    else:
        d = int(query[1])
        deleted = defaultdict(int)
        while len(S) > 0 and d > 0:
            c,x = S[0]
            if d > x:
                S.popleft()
                d -= x
                deleted[c] += x
            else:
                S[0][1] = x - d
                deleted[c] += d
                d = 0
        sum = 0
        for key in deleted:
            sum += deleted[key] ** 2
        ans.append(sum)

for i in range(len(ans)):
    print(ans[i])
