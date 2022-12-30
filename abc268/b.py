S = list(input())
T = list(input())

if len(S) > len(T):
    print("No")
    exit()

for i,c in enumerate(S):
    if c != T[i]:
        print("No")
        exit()
print("Yes")