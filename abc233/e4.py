X = input()

ans = (int(X)*10 // 9) - sum([int(c) for c in X])  // 9

print(ans)