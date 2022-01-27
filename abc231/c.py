N,Q = map(int,input().split())

A = list(map(int,input().split()))
x = []
for _ in range(Q):
    x.append(int(input()))

A.sort()
x_sorted = sorted(x)

count_short_than_x_j = [0 for _ in range(Q)]
i = 0
ans_dict = {}
for j in range(Q):
    temp = 0
    while i < N:
        if A[i] >= x_sorted[j]:
            break
        temp += 1
        i += 1
    count_short_than_x_j[j] = count_short_than_x_j[j-1] + temp
    ans_dict[x_sorted[j]] = count_short_than_x_j[j]

for j in range(Q):
    print(N-ans_dict[x[j]])

