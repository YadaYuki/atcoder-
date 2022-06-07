n = int(input())
p = list(map(int,input().split()))

one_idx = p.index(1)
ascending = p[(one_idx+1)%n] == 2

ans = None
if ascending:
    ans = min(one_idx,n-one_idx+2)
else:
    ans = min(one_idx+2,(n-one_idx-1) + 1)


print(ans)