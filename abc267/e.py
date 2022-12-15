from collections import deque
N,M = map(int,input().split())
A = list(map(int,input().split()))
graph = [[] for i in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)


def is_x_ok(x:int):
    queue = deque([])
    costs = [0 for i in range(N)]
    erased = [False for i in range(N)]
    for i in range(N):
        for n in graph[i]:
            costs[i] += A[n]
        if x >= costs[i]:
            queue.append(i)
            erased[i] = True


    while len(queue) > 0:
        cur = queue.popleft()
        
        # erase cur
        for n in graph[cur]:
            if erased[n]:
                continue
            costs[n] -= A[cur]
            if costs[n] <= x:
                queue.append(n)
                erased[n] = True
    
    ok = sum(erased) == len(erased)

    
    return ok
        

max_A = max(A)
ok,ng = max_A * N + 1,-1

while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_x_ok(mid):
        ok = mid
    else:
        ng = mid


print(ok)