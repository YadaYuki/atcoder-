from collections import deque,defaultdict
M = int(input())
G = [[] for _ in range(9)]

for _ in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

p = list(map(int,input().split()))

s_start = [str(0)] * 9

for j in range(8):
    s_start[p[j]-1] = str(j+1)


s_start = "".join(s_start)
s_goal = "123456780"

if s_start == s_goal:
    print(0)
    exit()

Q = deque()
Q.append(s_start)
cost_to_s = defaultdict(int)
cost_to_s[s_start] = 0


while len(Q) > 0:
    s = Q.popleft()
    s_list = list(s)
    empty_vertex = s_list.index("0")
    cost_to_s_next = cost_to_s[s] + 1
    for vertex in G[empty_vertex]: # コマが存在しない頂点と隣接する頂点
        s_next = s_list[:]
        s_next[vertex],s_next[empty_vertex] = s_next[empty_vertex],s_next[vertex]
        s_next = "".join(s_next)
        if s_next == s_goal:
            print(cost_to_s_next)
            exit()
        else:
            if s_next not in cost_to_s:
                cost_to_s[s_next] = cost_to_s_next
                Q.append(s_next)

print(-1)