X_str = input()
X = int(X_str)

ans = (10*X - sum([int(c) for c in X_str]))//9
print(ans)
