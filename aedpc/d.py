if __name__ == "__main__":
    N, W = map(int, input().split())
    w, v = [], []
    for _ in range(N):
        wi, vi = map(int, input().split())
        w.append(wi)
        v.append(vi)

    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for weight in range(1, W+1):
            if weight < w[i-1]:
                dp[i][weight] = dp[i-1][weight]
            else:
                dp[i][weight] = max(
                    dp[i-1][weight], v[i-1] + dp[i-1][weight-w[i-1]])
    print(dp[N][W])
