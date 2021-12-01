N,W = map(int,input().split())

cheese = []
for _ in range(N):
    A,B = map(int,input().split())
    cheese.append([A,B])

cheese.sort(reverse=True)

ans = 0
for item in cheese:
    A,B= item
    if B <= W:
        ans += A * B
        W -= B
    else:
        ans += A * W
        W = 0
        break

print(ans)
