N, W = map(int, input().split())

product = []

for _ in range(N):
    w, v = map(int, input().split())
    product.append([w, v])

price = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        w, v = product[i-1]
        price[i][j] = price[i-1][j]
        if j >= w:
            price[i][j] = max(price[i][j], price[i-1][j-w] + v)

print(price[N][W])
