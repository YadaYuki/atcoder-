from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

c = []

for i in range(R):
    c.append(input())


q = deque()

sy -= 1
sx -= 1
gy -= 1
gx -= 1


q.append([sy, sx])

cost = [[-1 for _ in range(C)] for _ in range(R)]
cost[sy][sx] = 0
while len(q) != 0:
    i, j = q.popleft()
    for i_next_to, j_next_to in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if 0 < i_next_to < R and 0 < j_next_to < C:
            if c[i_next_to][j_next_to] == "." and cost[i_next_to][j_next_to] == -1:
                cost[i_next_to][j_next_to] = cost[i][j] + 1
                q.append([i_next_to, j_next_to])

print(cost[gy][gx])
