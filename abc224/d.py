from collections import deque,defaultdict

M = int(input())
graph = []
NODE_NUM = 9

for _ in range(NODE_NUM):
    graph.append([])

for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

initial_coma_order = list("999999999")

p = list(map(int,input().split()))
for i in range(len(p)):
    initial_coma_order[p[i]-1] = str(i + 1)

initial_coma_order = "".join(initial_coma_order)

Q = deque()

Q.append(initial_coma_order)


cost = defaultdict(int)
cost[initial_coma_order] = 0

if initial_coma_order == "123456789":
    print(0)
    exit(0)

while len(Q) > 0:
    coma_order = Q.popleft()
    # 駒が存在しないノードを探索する
    node_not_coma = -1
    for i in range(NODE_NUM):
        if coma_order[i] == "9":
            node_not_coma = i
            break
    
    # 駒が存在しないノードと隣接するノードは交換可能。Qにpushし、costも計算する。

    cost_to_coma_order = cost[coma_order]
    coma_order = list(coma_order)

    for node in graph[node_not_coma]:
        coma_order_exchanged = coma_order[:]
        coma_order_exchanged[node],coma_order_exchanged[node_not_coma] = coma_order_exchanged[node_not_coma],coma_order_exchanged[node]
        coma_order_exchanged = "".join(coma_order_exchanged)
        if cost[coma_order_exchanged] == 0:
            cost[coma_order_exchanged] = cost_to_coma_order + 1
            Q.append(coma_order_exchanged)


if cost["123456789"] == 0:
    print(-1)
else:
    print(cost["123456789"])









