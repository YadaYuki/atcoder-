from collections import defaultdict,deque

next_grid = {}
visited = {}

N = int(input())
XY = list()
for i in range(N):
    X,Y = map(int,input().split())
    XY.append((X,Y))
    visited[(X,Y)] = False
    next_grid[(X,Y)] = [(X-1,Y-1),(X-1,Y),(X,Y-1),(X,Y+1),(X+1,Y),(X+1,Y+1)]

ans = 0
for i in range(N):
    X,Y = XY[i]
    if visited[(X,Y)] == False:
        ans += 1
        # BFS
        s = (X,Y)
        visited[s] = True
        q = deque([s])

        while len(q) > 0:
            cur = q.popleft()
            for n in next_grid[cur]:
                if n not in next_grid:
                    continue
                if visited[n]:
                    continue
                
                visited[n] = True
                q.append(n)

print(ans)



