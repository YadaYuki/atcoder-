import itertools


N,M = map(int,input().split())

ans = list(itertools.combinations([i for i in range(1,M+1)], N))
for i in ans:
    print(*i)
