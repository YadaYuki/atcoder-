N = int(input())
H = list(map(int, input().split()))

for i in range(N):
    if i == N-1:
        print(H[i])
        exit()
    if not H[i] < H[i+1]:
        print(H[i])
        exit()