l1,r1,l2,r2 = map(int,input().split())

lm = max(l1,l2)
rmi = min(r1,r2)
ans = max(rmi - lm,0)
print(ans)

