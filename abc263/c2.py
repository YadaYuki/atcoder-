from itertools import combinations

N,M = map(int,input().split())

ans = combinations([i for i in range(1,M+1)], N)

for a in ans:
    print(*a)

