from collections import defaultdict,deque

M = int(input())

graph = []

for _ in range(9):
    graph.append([])

for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

p = list(map(int,input().split()))

coma_in_graph = list("999999999")

for i in range(8):
    coma_in_graph[p[i]-1] = str(i + 1)

coma_in_graph_dict = defaultdict(int)

cost["".join(coma_in_graph)] = 0

queue = deque()

queue.append("".join(coma_in_graph))

count = 0

while len(queue) > 0:
    coma_in_graph = queue.popleft()


    coma_in_graph = list(coma_in_graph)
    # コマがないノードと接続しているノードに存在するコマをコマがないノードに移動する。
    not_coma = -1
    for i in range(9):
        if coma_in_graph[i] == "9":
            not_coma = i
    # 移動した後の状態をqueueにappendする
    for next_node in graph[not_coma]:
        coma_in_graph_after_move = coma_in_graph[:]
        coma_in_graph_after_move[not_coma],coma_in_graph_after_move[next_node] = coma_in_graph_after_move[next_node],coma_in_graph_after_move[not_coma]
        queue.append("".join(coma_in_graph_after_move))
        count += 1











