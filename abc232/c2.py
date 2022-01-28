from itertools import permutations
N,M = map(int, input().split())

g1,g2 = [[False for _ in range(N)] for _ in range(N)],[[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    g1[a-1][b-1] = True
    g1[b-1][a-1] = True

for _ in range(M):
    a,b = map(int, input().split())
    g2[a-1][b-1] = True
    g2[b-1][a-1] = True


patterns = list(permutations([i for i in range(N)]))



for pattern in patterns:
    is_same = True
    for i in range(N):
        for j in range(N):
            if g1[i][j] != g2[pattern[i]][pattern[j]]:
                is_same = False
    if is_same:
        print("Yes")
        exit()

print("No")

