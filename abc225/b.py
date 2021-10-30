N = int(input())

tree = []

for _ in range(N):
    tree.append([])

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

for i in range(N):
    if len(tree[i]) == N-1:
        print("Yes")
        exit(0)

print("No")
    



