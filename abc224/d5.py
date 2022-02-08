from collections import defaultdict,deque
M = int(input())
graph = [[] for _ in range(9)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

p = list(map(int,input().split()))

coma_in_nodes = list('000000000')

for j in range(8):
    coma_in_nodes[p[j]-1] = str(j+1)

coma_in_nodes = ''.join(coma_in_nodes)
if coma_in_nodes == '123456780':
    print(0)
    exit()

cost_to_s = {}
cost_to_s[coma_in_nodes] = 0
queue = deque([coma_in_nodes])

while len(queue) > 0:
    coma_in_nodes_str= queue.popleft()
    cost_to_prev = cost_to_s[coma_in_nodes_str]
    coma_in_nodes = list(coma_in_nodes_str)
    empty_node = coma_in_nodes.index('0')
    # 空のノードと隣接するノードを取得
    for node in graph[empty_node]:
        coma_in_nodes_next = coma_in_nodes[:]
        coma_in_nodes_next[node],coma_in_nodes_next[empty_node] \
            = coma_in_nodes_next[empty_node],coma_in_nodes_next[node]
        coma_in_nodes_next = ''.join(coma_in_nodes_next)
        if coma_in_nodes_next == '123456780':
            print(cost_to_prev + 1)
            exit()
        else:
            if coma_in_nodes_next not in cost_to_s:
                cost_to_s[coma_in_nodes_next] = cost_to_prev + 1
                queue.append(coma_in_nodes_next)

print(-1)



