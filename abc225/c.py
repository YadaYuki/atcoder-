
N,M = map(int,input().split())

B = []

for _ in range(N):
    B.append(list(map(int,input().split())))


is_valid = True

# 7の倍数より右に値がない
for i in range(M-1):
    if B[0][i] % 7 == 0:
        print("No")
        exit(0)

# 横方向に差が1である。
for i in range(N):
    for j in range(1,M):
        if B[i][j] - B[i][j-1] != 1:
            print("No")
            exit(0)

# 横方向に差が7である。
for i in range(1,N):
    for j in range(M):
        if  B[i][j] - B[i-1][j] != 7:
            print("No")
            exit(0)




print("Yes")


