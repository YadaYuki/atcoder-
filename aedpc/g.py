import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
is_starting_point = [True] * N  # 入ってくる辺があるかどうか.

for i in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    is_starting_point[y-1] = False


done = [False] * N # 結果をメモ化することによって無駄な再計算をなくすことができるんです。
longest_path = [-1] * N

def get_longest_path(node: int):
    if len(graph[node]) == 0:
        return 0
    else:
        global longest_path,done
        if done[node] == True:
          return longest_path[node]
        
        for node_next_to in graph[node]:
            longest_path[node] = max(longest_path[node], get_longest_path(node_next_to)+1)
        done[node] = True
        return longest_path[node]


ans = -1

for i in range(N):
    if is_starting_point[i]:
        ans = max(ans, get_longest_path(i))

print(ans)
