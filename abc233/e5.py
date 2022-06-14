X_str = input()
bit_sum = sum([int(c) for c in X_str])
ans = 10 * int(X_str) // 9 - bit_sum // 9
print(ans)

