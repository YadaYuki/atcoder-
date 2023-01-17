X,K = map(int,input().split())
for i in range(K):
    n = 10 ** (i + 1)
    if X % n // (n//10) >= 5:
        X = (X // n + 1) * n
    else:
        X = (X // n) * n
print(X)

