X,Y,N = map(int,input().split())
ans = min((N//3) * Y + (N%3)*X,N * X)
print(ans)

