import sys
sys.setrecursionlimit(10 ** 6)

N,M = map(int,input().split())

graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    if len(graph[i]) > 2: # 二人以上と隣り合うことはできない
        print('No')
        exit(0)

visited = [False for _ in range(N)]
# 閉路が存在する場合はNg 
def has_cycle_dfs(prev_node,cur_node):
    visited[cur_node] = True
    for next_node in graph[cur_node]:
        if next_node != prev_node:
            if visited[next_node]:
                return True
            else:
                return has_cycle_dfs(cur_node,next_node)

    return False

if has_cycle_dfs(-1, 0):
    print("No")
    exit(0)

print("Yes")