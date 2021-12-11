T = list('oxx' * (10 ** 5))
S = input()
for i in range(len(T) - len(S) + 1):
    if "".join(T[i:i+len(S)]) == S:
        print("Yes")
        exit(0)

print("No")
