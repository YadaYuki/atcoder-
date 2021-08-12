N = int(input())
A = list(map(int,input().split()))

hash = {}

for i in range(N):
  hash[A[i]] = i+1

A.sort()

print(hash[A[-2]])
