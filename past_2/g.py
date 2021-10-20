from collections import deque
from string import ascii_lowercase

Q = int(input())
que = deque()

for i in range(Q):
    query = input().split()
    if query[0] == "1":
        c,x = query[1],int(query[2])
        que.append([c,x])
    else:
        d = int(query[1])

        c_count = {}
        for c in ascii_lowercase:
            c_count[c] = 0
        
        while d > 0 and len(que) > 0:
            c,x = que[0] # 参照しかしない.
            if d >= x :
                d -= x
                c_count[c] += x
                que.popleft()
            else:
                c_count[c] += d
                que[0][1] -= d
                d = 0
        
        ans = 0
        for c in ascii_lowercase:
            ans += c_count[c] ** 2
        print(ans)
