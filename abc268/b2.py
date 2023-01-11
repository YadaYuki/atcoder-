S = list(input())
T = list(input())
if len(S) > len(T):
    print("No")
    exit()

for i in range(len(S)):
    if S[i] != T[i]:
        print("No")
        exit()

print("Yes")