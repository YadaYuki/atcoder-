N = int(input())
A = list(map(int,input().split()))

point_to_id = {}

for i in range(N):
    point_to_id[A[i]] = i

A.sort()

print(point_to_id[A[-2]] + 1)
